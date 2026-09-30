# [LEGACY] from data_extraction import eredes_data, eredes_metadata  # moved to legacy/eredes-selenium-extractor/
from data_processing import eredes_merge_files, eredes_final_format


def eredes_main() -> None:
    """
    Main function to execute the Eredes data processing pipeline.

    This function calls several main functions from different modules
    responsible for data extraction, metadata handling, merging files,
    and formatting the final output. Any errors encountered during 
    execution are printed to the console.
    """
    # [LEGACY] try:
    # [LEGACY]     eredes_data.main()
    # [LEGACY] except Exception as e:
    # [LEGACY]     print(f"Error in eredes_data.main(): {e}")

    # [LEGACY] try:
    # [LEGACY]     eredes_metadata.main()
    # [LEGACY] except Exception as e:
    # [LEGACY]     print(f"Error in eredes_metadata.main(): {e}")

    try:
        eredes_merge_files.main()
    except Exception as e:
        print(f"Error in eredes_merge_files.main(): {e}")

    try:
        eredes_final_format.main()
    except Exception as e:
        print(f"Error in eredes_final_format.main(): {e}")

        

if __name__ == "__main__":
    eredes_main()
