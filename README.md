# Portugal Energy Transition

![Python](https://img.shields.io/badge/language-python-blue)
![Repo size](https://img.shields.io/github/repo-size/rogernogueraplanesas/portugal-energy-transition)
![Last commit](https://img.shields.io/github/last-commit/rogernogueraplanesas/portugal-energy-transition)

Data project on **Portugal's energy transition and the regional adoption of renewables**,
using distribution-grid data from **E-REDES** and placing it in a European context with
**socioeconomic indicators from Eurostat**.

## Research question

> **Is the adoption of renewables across Portuguese regions associated with socioeconomic
> factors, and how does Portugal compare with the broader European pattern?**

The idea is to cross regional grid/energy data for Portugal (E-REDES) with socioeconomic
indicators (Eurostat) to see whether renewable adoption tracks factors such as income,
population or economic activity — and to benchmark Portugal against other European regions.

## Background

This project started in **2023–2024** as work done during an **internship** (early in my
data-science path). That first version worked but was limited; I put real effort into its
documentation (several READMEs, images, a data-flow GIF).

In **2026** I'm picking it back up **on my own, as a personal / portfolio project** — with
no relation to that company or to any formal studies. The goal now is to turn the existing
multi-source ingestion work into a clean analytical project.

## Roadmap

The work is organized in phases. **Only the current phase is active** — the rest are planned.

1. **Phase 1 — EDA (current):** exploratory analysis of the E-REDES × Eurostat data to
   probe the research question above.
2. **Phase 2 — ML pipeline (planned):** modelling on top of the cleaned data.
3. **Phase 3 — Refactor (planned):** production hardening — type hints, tests, and a CLI.

## Data sources

| Source | Role |
|---|---|
| [E-REDES](https://e-redes.opendatasoft.com/explore/?sort=modified) | Portuguese distribution-grid / energy indicators (analytical core) |
| [Eurostat](https://ec.europa.eu/eurostat/data/database) | European socioeconomic indicators (context / comparison) |
| [INE Portugal](https://www.ine.pt/) | Portuguese national statistics |
| [World Bank](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation) | Additional macro indicators |

Data is stored in **SQLite** for now. Detailed, per-source method notes live in [`docs/`](docs/).

## Project structure (indicative)

> This layout is inherited from the original build and is a **starting point** — it may be
> reorganized as the analytical phases progress.

```
portugal-energy-transition/
├── app/
│   ├── api/                  # FastAPI layer from the original build (auth, data, users)
│   ├── db/                   # SQLite creation/loading + E-R diagrams
│   ├── indicators_data/      # Core: extraction → processing → loading, per source
│   │   ├── eredes/           #   E-REDES   (API extraction / inspection / cleaning; old processing / loading)
│   │   ├── eurostat/         #   Eurostat  (API extraction / inspection / cleaning; old processing / loading)
│   │   ├── ine/              #   INE PT    (API extraction / inspection / cleaning; old processing / loading)
│   │   ├── worldbank/        #   World Bank(extraction / processing / loading)
│   │   └── data_main.py      #   orchestrator
│   └── utils/                # Geographic reference table (concelho_codes/), old location codes, method PDFs
├── docs/                     # Per-source guides (*.md) and images
├── legacy/                   # Retired approaches kept as samples
│   ├── eredes-selenium-extractor/   # 2023–2024 Selenium bot (superseded by E-REDES API)
│   ├── eurostat-client-extractor/   # 2024 bulk TOC download + metadata scraping
│   └── ine-api-extractor/           # 2024 bulk download of ~260 INE indicators
├── requirements.txt
└── README.md
```

The E-REDES, Eurostat and INE sources are being rebuilt in phases. Each one uses
`source_inspection/` (explore the catalogue), `data_extraction/get_raw_data.py`
(download the hand-picked datasets → `data_raw/`), `data_inspection/` and
`data_eda/00_data_cleaning.ipynb` (→ `data_interim/`). The original `data_processing/`,
`data_load/` and `*_main.py` are kept as reference and are not wired to the new steps yet.
`data_raw/` and `data_interim/` are git-ignored and generated locally.

## Workflow

| # | Step | Where | Output | Status |
|---|---|---|---|---|
| 0 | Explore each source's catalogue | `source_inspection/`, `ine/data_extraction/get_catalogue.py` | catalogue in `data_raw/` | ✅ |
| 1 | Download the selected datasets | `data_extraction/get_raw_data.py` | `data_raw/` | ✅ |
| 2 | Inspect them (shape, types, nulls, duplicates) | `data_inspection/datasets_inspection.ipynb` | — | ✅ |
| 3 | First cleaning: types, nulls, normalized codes, common `cod_concelho` | `data_eda/00_data_cleaning.ipynb` | `data_interim/` | ✅ |
| 4 | Geographic reference table (INE + E-REDES, cross-validated) | [`app/utils/concelho_codes/`](app/utils/concelho_codes/) | `concelho_reference.csv` | ✅ |
| 5 | Univariate EDA per dataset | `data_eda/` | — | next |
| 6 | Decide metrics, columns and representation per indicator | — | — | |
| 7 | Joint dataset: join on `cod_concelho`, names and levels from the reference table | — | — | |
| 8 | Bivariate EDA on the joint dataset | — | — | |
| 9 | Load into the database and serve through the API | `app/db/`, `app/api/` | — | |

Eurostat follows its own track: its datasets are country-level (comparison of Portugal with
other EU countries), so it does not use the reference table or the joint concelho dataset.

## Setup

```bash
pip install -r requirements.txt
```

> A virtual environment (venv) is recommended.

## Notes

- The **E-REDES Selenium extractor** used in 2023–2024 now lives under
  [`legacy/`](legacy/eredes-selenium-extractor/); E-REDES has since offered an official
  open-data API, which is the intended way to ingest its data going forward.
- The original **Eurostat** and **INE** bulk extractors (2024) also moved to `legacy/`
  ([Eurostat](legacy/eurostat-client-extractor/), [INE](legacy/ine-api-extractor/)); they
  were replaced by small extractors that download only hand-picked datasets.
- Territorial codes and names differ between sources. How they are reconciled (and why
  datasets are joined on codes, never on names) is documented in
  [`app/utils/concelho_codes/`](app/utils/concelho_codes/README.md).
- Git history from the original build is kept as-is.
