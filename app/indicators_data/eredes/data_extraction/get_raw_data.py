import requests
from pathlib import Path

DATASETS = [
    "8-total-upac-mensal",
    "energia_injectada_upac",
    "26-centrais",
    "comunidades-de-energia",
    "codigo-de-atividade-economica-por-distrito-concelho-e-freguesia",
    "clientes-por-escalao-de-potencia",
    "25-plr-producao-renovavel"
] # Manual selection (website data exploration)

raw_data_folder = Path(__file__).resolve().parent.parent / "data_raw" # .parent.parent locates the path to the eredes folder (2 above) then the raw data folder name is indicated


def get_save_datasets():
    """Download E-REDES datasets as CSV files into the data_raw folder."""
    raw_data_folder.mkdir(parents=True, exist_ok=True)
    failed = [] # Datasets that could not be downloaded

    for dataset in DATASETS:
        print(f"Downloading dataset: {dataset}")

        try:
            url = f"https://e-redes.opendatasoft.com/api/explore/v2.1/catalog/datasets/{dataset}/exports/csv"
            response = requests.get(url, timeout=60)
            response.raise_for_status()

            savepath = raw_data_folder / f"{dataset}.csv"

            with open(savepath, 'wb') as file:
                file.write(response.content)

            print(f"Dataset correctly saved: {dataset}")

        except requests.RequestException as error:
            print(f"Error downloading {dataset}: {error}")
            failed.append(dataset)

    if failed:
        print(f"Finished with errors. Not downloaded: {failed}")
    else:
        print("All datasets downloaded.")


if __name__ == "__main__":
    get_save_datasets()