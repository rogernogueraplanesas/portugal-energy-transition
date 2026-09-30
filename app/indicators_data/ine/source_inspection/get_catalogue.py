import requests
from pathlib import Path
import os
import xml.etree.ElementTree as ET
import json



catalog_folder = Path(__file__).resolve().parent.parent / "data_raw"

def element_to_dict(element):
    """
    Convert an XML element into either:
    - its text, if it has no child elements
    - a dictionary, if it contains child elements
    """

    if len(element) == 0: # No mira longitud del texto, mira número de tags dentro
        return element.text # text que no tag

    result = {}
    for child in element:
        result[child.tag] = element_to_dict(child) # Llena el dict con claves hasta llegar al último nivel donde devuelve texto
    return result # Devuelve un diccionario con tantos niveles como tenga cada elemento del indicador


def get_catalogue(url: str):
    catalog_data = {}
    response = requests.get(url=url, timeout=60)
    response.raise_for_status()
    root = ET.fromstring(response.content)
    for indicator in root.findall(".//indicator"): # // to find at any level below 'root'
        indicator_id = indicator.get("id")
        indicator_data = {}
        for child in indicator: # Direct sublevels inside each 'indicator'
            indicator_data[child.tag] = element_to_dict(child) # tag es nombre de la etiqueta como 'title'
        catalog_data[indicator_id] = indicator_data
    return catalog_data

def save_catalog_data(catalog_folder, catalog_data):
    catalog_folder.mkdir(parents=True, exist_ok=True) # como 'catalog_folder es un path evitamos el os.makesdir()
    with open(catalog_folder/"ine_catalog.json", 'w', encoding='utf-8') as file:
        json.dump(catalog_data, file, indent=4, ensure_ascii=False)
    print(f"Catalog saved in {catalog_folder}")



if __name__=="__main__":
    # opc = 3 --> Main indicators (aprox. 260 out of 10,000 indicators)
    url = "https://www.ine.pt/ine/xml_indic.jsp?opc=3&lang=EN" # XML data to be converted into JSON
    catalog_data = get_catalogue(url)
    save_catalog_data(catalog_folder, catalog_data)