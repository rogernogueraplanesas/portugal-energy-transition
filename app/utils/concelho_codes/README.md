# Geographic reference table (concelhos)

`create_concelho_map.ipynb` builds **`concelho_reference.csv`**: one row per Portuguese
concelho (308) with every territorial level above it, as codes and names.

| Level | Code column | Name column | Source |
|---|---|---|---|
| Concelho | `cod_concelho` | `concelho` | INE |
| Distrito / island | `cod_distrito` | `distrito` | E-REDES (islands: see below) |
| NUTS III | `cod_nuts_iii` | `nuts_iii` | INE |
| NUTS II | `cod_nuts_ii` | `nuts_ii` | INE |
| NUTS I | `cod_nuts_i` | `nuts_i` | INE |
| Country | `cod_pais` | `pais` | INE |

**Project rule:** datasets are always joined on `cod_concelho`, never on names. Names for any
level are taken from this table.

Read it keeping every column as text, so codes keep their leading zeros:

```python
pd.read_csv("concelho_reference.csv", dtype=str)
```

## When it runs

After the `data_eda/00_data_cleaning.ipynb` notebooks of **INE** and **E-REDES**, because it reads
their `data_interim/` files (normalized codes and the `cod_concelho` column). The table is then
used when the joint dataset is built, after the univariate EDA. Eurostat is not involved: its
datasets are country-level.

## Codes in each source

| Source | Column | Format | Example |
|---|---|---|---|
| E-REDES | `cod_concelho` (renamed from `codconcelho`, `codigo_concelho`, `con_code`) | 4-digit DICO code | `1804` |
| INE | `geocod` | Hierarchical NUTS 2024 code; its length gives the level | `11C1804` |
| Eurostat | `geo` | Country code | `PT` |

INE `geocod` levels:

| Length | Level | Example |
|---|---|---|
| `PT` | Country | Portugal |
| 1 | NUTS I | `1` Continente |
| 2 | NUTS II | `11` Norte |
| 3 | NUTS III | `11C` Tâmega e Sousa |
| 7 | Concelho | `11C1804` Cinfães = NUTS III `11C` + concelho `1804` |

The last 4 characters of a concelho `geocod` are the same DICO code E-REDES uses, so INE's
`cod_concelho` is extracted directly from it (INE cleaning notebook). The first 2 digits of the
DICO code are the distrito (`1804` → `18` Viseu).

## What was checked (and is re-checked in the notebook)

- **INE coverage:** 308 concelhos with 308 distinct codes. Both INE datasets (income per
  inhabitant and population density) contain exactly the same `geocod` values.
- **E-REDES vs INE codes:** every concelho code in the 7 E-REDES datasets exists in INE. Six of
  them cover 278 concelhos or fewer because E-REDES only operates in mainland Portugal;
  `atividade_economica` covers all 308, islands included.
- **NUTS III:** the NUTS III code E-REDES gives for each concelho (`atividade_economica`) matches
  INE for all 308 concelhos.
- **Names, code by code:** they match apart from letter case and 4 cases in
  `atividade_economica`: *Calheta de São Jorge* vs *Calheta (R.A.A.)*, *Lagoa* vs
  *Lagoa (R.A.A.)*, *Praia da Vitória* vs *Vila da Praia da Vitória*, and *Calheta* vs
  *Calheta (R.A.M.)*.
- **Why not join on names:** there are two *Lagoa* (Algarve `0806` and Açores `4201`) and two
  *Calheta* (Madeira `3101` and Açores `4501`). A merge on names would mix them up.

## Distritos and islands

Distrito and NUTS are **parallel hierarchies**: a distrito can be split across several NUTS
regions, so neither hangs from the other. Both are linked only through the concelho, which is
why the table has one row per concelho.

In Madeira and the Açores distritos no longer exist as an administrative division (abolished
in 1976), and in the DICO coding the first 2 digits identify the **island** instead. E-REDES
leaves those names empty, so for codes `31`–`32` and `41`–`49` the `distrito` column holds the
island name (e.g. `42` → Ilha de São Miguel). The notebook lists the concelhos of each code
before assigning them, so the mapping can be checked.

## Levels not included

**Freguesia** is left out on purpose: only E-REDES provides it (INE does not in these datasets),
and the 2025 freguesia reorganization restored around 300 previously merged freguesias, so it
could not be validated against a second source.
