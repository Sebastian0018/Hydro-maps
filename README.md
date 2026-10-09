# Hydro Maps — #30DayMapChallenge, hydrology edition

Maps about water in and around Boston, made while learning Python for geospatial data. I'm a civil engineer who specialized in hydro-technics (Pontificia Universidad Javeriana), and a Python **beginner**. These maps are how I'm practicing, following [Milán Janosov's 30-Day Map Challenge tutorials](https://milanjanosov.substack.com/p/30-days-30-maps-my-full-30daymapchallenge-26f) and applying them to hydrology.

| # | Map | Question | Skills | Data |
|---|-----|----------|--------|------|
| 01 | [Stream gauges](01-points/) | Where are Massachusetts' rivers measured, and how many monitoring sites are still active? | GeoPandas, matplotlib, contextily | USGS Water Data · *in progress* |
| 02 | [Charles River sinuosity](02-lines/) | How much does the Charles River meander between its source and Boston Harbor? | osmnx, projections, line lengths | OpenStreetMap · *in progress* |

## Roadmap (October)

- **03** — Rivers of New England, line width by stream order (HydroRIVERS)
- **04** — River basins of New England, rivers colored by basin (HydroBASINS + HydroRIVERS)
- **05** — 3D relief of the Charles River basin (DEM + forge3d)

Goal: combine 03 + 04 + 05 into one Milos-style New England map (basin colors + shaded relief + rivers by order). Style inspired by [Milos Popovic](https://github.com/milos-agathon)'s river and terrain maps (he works mostly in R; I'm reproducing the ideas in Python).

## Run it yourself

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
jupyter lab
```

Each folder has a `notebook.ipynb` that downloads its own public data, so no large files live in this repo.

## Credits

- Tutorials: Milán Janosov, *30-Day Map Challenge*.
- Data: U.S. Geological Survey (USGS) Water Data; © OpenStreetMap contributors (ODbL); basemap: Esri World Gray Canvas (Esri, HERE, Garmin, © OpenStreetMap contributors).
- I write the code myself; an AI tutor (Claude Code) helps with hints, explanations and code review, and set up this repo's structure.
