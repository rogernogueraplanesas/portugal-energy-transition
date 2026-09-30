import eurostat
from pathlib import Path

raw_data_path = Path(__file__).resolve().parent.parent / "data_raw"

DATASETS = ['nrg_ind_ren', 'nrg_pc_204'] # Manual selection (website exploration)

def get_save_datasets():
        raw_data_path.mkdir(parents=True, exist_ok=True)
        failed = [] # Datasets that could not be downloaded

        for dataset in DATASETS:
            save_path = raw_data_path / f"{dataset}.csv"

            try:
                df = eurostat.get_data_df(dataset)
                df.to_csv(save_path, index = False, encoding='utf-8')
                print(f"Dataset {dataset} saved in {save_path}")

            except Exception as e:
                 print(f"Error saving {dataset} dataset: {e}")
                 failed.append(dataset)

        if failed:
            print(f"Finished with errors. Not saved: {failed}")
        else:
            print("Datasets saved. Process completed.")



if __name__ == "__main__":
    get_save_datasets()