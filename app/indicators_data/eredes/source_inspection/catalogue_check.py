from pathlib import Path
import requests
import json

def print_catalog():
    url = "https://e-redes.opendatasoft.com/api/explore/v2.1/catalog/datasets"
    response = requests.get(url)
    print(response.status_code)
    data = response.json()
    print(data)


def download_catalog():
    url = "https://e-redes.opendatasoft.com/api/explore/v2.1/catalog/exports/json"
    response = requests.get(url)
    data = response.json()
    raw_data_folder = Path(__file__).resolve().parent.parent / "data_raw"
    raw_data_folder.mkdir(parents=True, exist_ok=True)
    save_path = raw_data_folder / "eredes_catalog.json"
    with open(save_path, "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    download_catalog()