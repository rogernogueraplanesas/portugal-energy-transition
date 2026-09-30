# Legacy — INE bulk extractor (2024)

This folder holds the **original INE (Statistics Portugal) extractor**, written in **2024**
as part of the first build of the project.

`ine_api.py` downloaded the INE catalogue of main indicators (XML, `opc=3`, ~260 indicators)
and then requested the **data and metadata of every indicator** in it through the INE JSON
API, saving one JSON file per indicator.

## Why it is here and not in the active pipeline

The rebuilt pipeline splits this into two small steps and **selects indicators by hand**:

- [`get_catalogue.py`](../../app/indicators_data/ine/data_extraction/get_catalogue.py) —
  downloads the catalogue (keeping its nested XML structure) for exploration.
- [`get_raw_data.py`](../../app/indicators_data/ine/data_extraction/get_raw_data.py) —
  downloads only the indicators chosen for the analysis.

Downloading ~260 indicators (plus metadata) was slow and left mostly unused data behind.

It is kept here, unchanged, as a **sample of bulk API extraction** (XML catalogue parsing,
skipping already-downloaded files, rate limiting).

## Notes

- The code is preserved **as-is**. It was moved out of
  `app/indicators_data/ine/data_extraction/` without modification, so it still imports
  `app.utils.settings` and computes the project root with `..` hops that are **not adjusted**
  for this new location — it is not meant to run from here.
- The old `ine_main.py`, `data_processing/` and `data_load/` still reference this module;
  they are part of the original pipeline being rebuilt and are expected to break in the
  meantime.
