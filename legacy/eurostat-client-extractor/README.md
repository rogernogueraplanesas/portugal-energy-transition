# Legacy — Eurostat bulk extractor (2024)

This folder holds the **original Eurostat extractor**, written in **2024** as part of the
first build of the project.

- `eurostat_client_data.py` downloaded the full Eurostat **Table of Contents** (TOC) and then
  requested **every dataset listed in it**, filtered to Portugal (`geo=PT`), through the
  `eurostatapiclient` package. Each dataset was saved as JSON, plus a CSV of codes and labels.
- `eurostat_get_metadata.py` scraped the Eurostat metadata pages (BeautifulSoup) to find the
  Portugal-specific metadata downloads, saved the links to CSV and downloaded/unzipped them.

## Why it is here and not in the active pipeline

The rebuilt pipeline no longer downloads the whole catalogue. Datasets are **selected by
hand** after exploring the catalogue, and downloaded with the `eurostat` package in
[`app/indicators_data/eurostat/data_extraction/get_raw_data.py`](../../app/indicators_data/eurostat/data_extraction/get_raw_data.py)
(catalogue exploration lives in `source_inspection/catalogue_check.py`). That approach is
simpler, faster and keeps only the data the analysis actually uses — including other EU
countries for comparison, which the old `geo=PT` filter excluded.

It is kept here, unchanged, as a **sample of bulk API extraction and metadata scraping**.

## Notes

- The code is preserved **as-is**. It was moved out of
  `app/indicators_data/eurostat/data_extraction/` without modification, so it still imports
  `app.utils.settings` and computes the project root with `..` hops that are **not adjusted**
  for this new location — it is not meant to run from here.
- The old `eurostat_main.py`, `data_processing/` and `data_load/` still reference these
  modules; they are part of the original pipeline being rebuilt and are expected to break
  in the meantime.
- `eurostatapiclient` is kept in `requirements.txt` only for this legacy code.
