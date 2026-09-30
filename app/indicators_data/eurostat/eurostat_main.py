# [LEGACY] from data_extraction import eurostat_client_data, eurostat_get_metadata  # moved to legacy/eurostat-client-extractor/
from data_processing import eurostat_datacodes, extract_xml_files, eurostat_join_codes, eurostat_final_data


def eurostat_main():
    # [LEGACY] try:
    # [LEGACY]     eurostat_client_data.main()
    # [LEGACY] except Exception as e:
    # [LEGACY]     print(f"Error: {e}")

    try:
        eurostat_datacodes.main()
    except Exception as e:
        print(f"Error: {e}")

    # [LEGACY] try:
    # [LEGACY]     eurostat_get_metadata.main()
    # [LEGACY] except Exception as e:
    # [LEGACY]     print(f"Error: {e}")


    # [LEGACY] Pause for manual metadata downloads (only needed by eurostat_get_metadata)
    # [LEGACY] user_input = input(
    # [LEGACY] "Metadata automatically downloaded. Please add the remaining files that could not be downloaded automatically.\n"
    # [LEGACY] "Check the manual links in eurostat/eurostat_data/eurostat_comp_files/manual_metadata.csv.\n"
    # [LEGACY] "Type 'continue' to proceed: ")
    # [LEGACY] while user_input.lower() != "continue":
    # [LEGACY]     user_input = input("Please type 'continue' to proceed: ")


    try:
        extract_xml_files.main()
    except Exception as e:
        print(f"Error: {e}")

    try:
        eurostat_join_codes.main()
    except Exception as e:
        print(f"Error: {e}")

    try:
        eurostat_final_data.main()
    except Exception as e:
        print(f"Error: {e}")
        

if __name__ == "__main__":
    eurostat_main()