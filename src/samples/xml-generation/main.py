from csv_to_xml_converter import CSVtoXMLConverter

if __name__ == "__main__":
    converter = CSVtoXMLConverter("/data/Electric_Vehicle_Population_Data.csv")
    # print(converter.to_xml_str())
    # Get the XML string
    xml_content = converter.to_xml_str()

    # Specify the file path where you want to save the XML
    output_file_path = "/data/output.xml"

    # Save the XML content to the specified file
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(xml_content)

    print(f"XML content has been saved to {output_file_path}")    
    
