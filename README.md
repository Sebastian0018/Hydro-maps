# Hydro Maps — #30DayMapChallenge, hydrology edition

Maps about water in and around Boston, made while learning Python for geospatial data. I'm a civil engineer who specialized in hydro-technics (Pontificia Universidad Javeriana), and a Python **beginner**. These maps are how I'm practicing, following [Milán Janosov's 30-Day Map Challenge tutorials](https://milanjanosov.substack.com/p/30-days-30-maps-my-full-30daymapchallenge-26f) and applying them to hydrology.

| # | Map | Question | Skills | Data |
|---|-----|----------|--------|------|
| 01 | [Stream gauges](01-points/) | Where are Massachusetts' rivers measured, and how many monitoring sites are still active? | GeoPandas, matplotlib, contextily | USGS Water Data · *in progress* |
| 02 | [Charles River sinuosity](02-lines/) | How much does the Charles River meander between its source and Boston Harbor? | osmnx, projections, line lengths | OpenStreetMap · *in progress* |
| 03 | [Rivers of New England](03-rivers/) | How is New England's river network organized, from headwater streams to main stems? | bbox loading, CRS, clipping, styling by column, custom fonts | HydroRIVERS v1.0 · US Census Bureau · **done** |
| 04 | [River basins of New England](04-int_map/) | Which basin does each New England river drain to? | joins, Pfafstetter codes, custom colormaps | HydroBASINS v1c · HydroRIVERS v1.0 · **static done**, interactive next |

## Roadmap (October)

- **04** — Interactive version of the basins map (folium)
- **05** — 3D relief of the Charles River basin (DEM + forge3d)

Goal: combine 03 + 04 + 05 into one Milos-style New England map (basin colors + shaded relief + rivers by order). Style inspired by [Milos Popovic](https://github.com/milos-agathon)'s river and terrain maps (he works mostly in R; I'm reproducing the ideas in Python).

## Run it yourself

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
jupyter lab
```

Each folder has a `notebook.ipynb`. Raw data is never committed: the notebook downloads it, or the folder README says where to download it and which `data/` folder to unzip it into.

## Credits

- Tutorials: Milán Janosov, *30-Day Map Challenge*.
- Data: U.S. Geological Survey (USGS) Water Data; © OpenStreetMap contributors (ODbL); HydroSHEDS / HydroBASINS v1c and HydroRIVERS v1.0 (Lehner & Grill 2013); U.S. Census Bureau cartographic boundaries; basemap: Esri World Gray Canvas (Esri, HERE, Garmin, © OpenStreetMap contributors).
- I write the code myself; an AI tutor (Claude Code) helps with hints, explanations and code review, and set up this repo's structure.
