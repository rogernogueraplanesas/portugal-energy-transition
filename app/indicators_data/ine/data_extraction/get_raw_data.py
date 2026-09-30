import requests
from pathlib import Path
import json
import time


# Manual selection (catalog exploration)
DATASETS = {
    "Income_inhabitant": "0012670",  # Income per inhabitant
    "pop_density": "0013189",  # Population density
}


def get_save_datasets(raw_data_folder: Path):
    raw_data_folder.mkdir(parents=True, exist_ok=True)
    failed = [] # Datasets that could not be downloaded

    for name, dataset in DATASETS.items():
        print(f"Downloading dataset: {dataset}")

        try:
            url = f"https://www.ine.pt/ine/json_indicador/pindica.jsp?op=2&varcd={dataset}&lang=EN"
            response  = requests.get(url, timeout=60)
            response.raise_for_status()
            data = response.json()

            savepath = raw_data_folder / f"{name}_{dataset}.json"
            with open(savepath, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

        except Exception as e:
            print(f"Unable to download dataset: {dataset}: {e}")
            failed.append(dataset)

        time.sleep(1)

    if failed:
        print(f"Finished with errors. Not downloaded: {failed}")
    else:
        print("All datasets downloaded.")


if __name__ == "__main__":
    raw_data_folder = Path(__file__).resolve().parent.parent / "data_raw"
    get_save_datasets(raw_data_folder)