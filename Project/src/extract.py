import pandas as pd
import xml.etree.ElementTree as ET
import glob
import os.path
from sqlalchemy import create_engine

from utilities import insert_to_table

columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']
folder = "data"

from params import conn_string, table_name

"""
extract from a given file type: csv, json, xml
"""

def extract_from_csv(file_to_process: str) -> pd.DataFrame: 
    dataframe = pd.read_csv(file_to_process) 
    return dataframe

def extract_from_json(file_to_process: str) -> pd.DataFrame:
    dataframe = pd.read_json(file_to_process,lines=True)
    return dataframe

def extract_from_xml(file_to_process: str) -> pd.DataFrame:
    dataframe = pd.DataFrame(columns = columns)
    tree = ET.parse(file_to_process) 
    root = tree.getroot() 
    for person in root: 
        car_model = person.find("car_model").text 
        year_of_manufacture = int(person.find("year_of_manufacture").text)
        price = float(person.find("price").text) 
        fuel = person.find("fuel").text 
        sample = pd.DataFrame({"car_model":car_model, "year_of_manufacture":year_of_manufacture, "price":price, "fuel":fuel}, index = [0])
        dataframe = pd.concat([dataframe, sample], ignore_index=True) 
    return dataframe

"""
extract from folder
"""

def extract() -> pd.DataFrame:
    extracted_data = pd.DataFrame(columns = columns) 
    #for csv files
    for csv_file in glob.glob(os.path.join(folder, "*.csv")):
        extracted_data = pd.concat([extracted_data, extract_from_csv(csv_file)], ignore_index=True)
    #for json files
    for json_file in glob.glob(os.path.join(folder, "*.json")):
        extracted_data = pd.concat([extracted_data, extract_from_json(json_file)], ignore_index=True)
    #for xml files
    for xml_file in glob.glob(os.path.join(folder, "*.xml")):
        extracted_data = pd.concat([extracted_data, extract_from_xml(xml_file)], ignore_index=True)
    return extracted_data

# run
def main():
    data = extract()
    insert_to_table(data, table_name)

main()