from functions.csv_to_xml_converter import CSVtoXMLConverter

def convert():
    CSVtoXMLConverter("/data/Electric_Vehicle_Population_Data.csv")
    # print(converter.to_xml_str())