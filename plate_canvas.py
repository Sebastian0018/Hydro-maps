"""One shared canvas for every map that goes into the portfolio's Maps page.

The Maps page lays one map over another to compare them. That only works if
every export has the same pixel size, shows the same area, and has the title
and credits in the same place. This module holds those numbers in ONE place,
so two notebooks can never drift apart.

How to use it in a notebook (the notebook lives one folder below this file):

    import sys
    sys.path.append("..")                  # lets Python find this file
    from plate_canvas import new_plate, finish_plate

    fig, ax = new_plate()                  # instead of plt.subplots(figsize=...)
    ...                                    # your .plot(ax=ax, ...) calls, unchanged
    finish_plate(fig, ax, kicker="...", title="...", note="...",
                 credit="...", path="my_map.png", title_color="lightgreen")

This is export plumbing, written with Claude Code. The map itself (data,
filters, joins, colors, line widths) stays in each notebook.
"""
import io
import math

import matplotlib.pyplot as plt
from PIL import Image

# ---- The canvas: set once, never per map ---------------------------------
FIG_SIZE = (9.5, 10.2)               # inches
DPI = 200                            # 9.5 x 10.2 in at 200 dpi = 1900 x 2040 px
BG = "#1a1a1a"                       # background color of every plate
FONT = "Montserrat"                  # each notebook registers the font files

# Where the map is allowed to be, as fractions of the figure:
# (left, bottom, width, height). 0 = left/bottom edge, 1 = right/top edge.
MAP_BOX = (0.02, 0.05, 0.96, 0.92)

# Title block and credits, in figure fractions: the same spot on every plate.
TITLE_X, TITLE_Y = 0.615, 0.355
CREDIT_X, CREDIT_Y = 0.02, 0.016

# The mapped area in longitude/latitude (EPSG:4326): (west, east, south, north).
# It is the bounding box of the six New England states plus a small margin:
#   states.total_bounds = [-73.7278, 40.9852, -66.9499, 47.4597]
# The numbers are written here on purpose (hard-coded), so the area is
# identical in every notebook, whatever layers that notebook loads.
EXTENT = (-73.90, -66.78, 40.85, 47.60)


def new_plate():
    """Create the empty figure and the map axes on the shared canvas."""
    fig = plt.figure(figsize=FIG_SIZE, dpi=DPI, facecolor=BG)
    ax = fig.add_axes(MAP_BOX)
    ax.set_facecolor(BG)
    ax.set_axis_off()
    return fig, ax


def finish_plate(fig, ax, kicker, title, note, credit, path, title_color):
    """Fix the map area, write the title block and credits, save the PNG.

    kicker       small line above the title, e.g. "Rivers by stream order"
    title        the big line, e.g. "NEW ENGLAND"
    note         small grey line under the title ("" for none)
    credit       data credits, bottom left (use "\\n" for a second line)
    path         file to save, e.g. "ne_rivers.png"
    title_color  color of the big line
    """
    # geopandas' .plot() changes the limits and the aspect of the axes every
    # time it draws a layer, so they are set here, after all the plotting.
    west, east, south, north = EXTENT
    ax.set_xlim(west, east)
    ax.set_ylim(south, north)
    # In lon/lat one degree of longitude is narrower than one degree of
    # latitude. This stretch corrects it at the middle latitude of the map.
    mid_lat = (south + north) / 2
    ax.set_aspect(1 / math.cos(math.radians(mid_lat)))

    # fig.text() works in figure fractions, so the text cannot move with the data.
    fig.text(TITLE_X, TITLE_Y + 0.036, kicker, color="lightgray", fontfamily=FONT,
             fontweight="light", fontsize=15, ha="left", va="baseline")
    fig.text(TITLE_X, TITLE_Y, title, color=title_color, fontfamily=FONT,
             fontweight="bold", fontsize=25, ha="left", va="baseline")
    fig.text(TITLE_X, TITLE_Y - 0.024, note, color="#6b6b6b", fontfamily=FONT,
             fontweight="light", fontsize=8.5, ha="left", va="baseline")
    fig.text(CREDIT_X, CREDIT_Y, credit, color="#585757", fontfamily=FONT,
             fontweight="light", fontsize=8, ha="left", va="bottom", linespacing=1.5)

    save_clean_png(fig, path)
    return path


def save_clean_png(fig, path):
    """Save the figure at the full canvas size, without metadata.

    No bbox_inches="tight" here: "tight" crops each map to its own content,
    and that is what gave every export a different size.
    """
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=DPI, facecolor=BG)
    buf.seek(0)
    img = Image.open(buf)
    # Copy only the pixels into a new image: this drops the metadata that
    # matplotlib writes into the file (software name and version).
    Image.frombytes(img.mode, img.size, img.tobytes()).save(path, "PNG", optimize=True)
    print("saved", path, img.size)
