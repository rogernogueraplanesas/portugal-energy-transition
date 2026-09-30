import eurostat
from pathlib import Path

raw_data_path = Path(__file__).resolve().parent.parent / "data_raw"

def print_catalog():
    """ Print the Eurostat catalogue """
    toc = eurostat.get_toc()
    print(toc)


def save_catalog_csv():
    """ Download the Eurostat catalogue and save it as a CSV file"""

    try:
        raw_data_path.mkdir(parents=True, exist_ok=True)

        toc_df = eurostat.get_toc_df()

        save_path = raw_data_path / "eurostat_catalog.csv"

        toc_df.to_csv(save_path, index= False, encoding='utf-8')

        print(f"Catalogue saved: {save_path}")

    except Exception as e:
        print(f"Error saving Eurostat toc as CSV: {e}")



if __name__ == "__main__":
    save_catalog_csv()