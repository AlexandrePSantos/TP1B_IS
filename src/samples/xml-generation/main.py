""" from csv_to_xml_converter import CSVtoXMLConverter
from lxml import etree

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

    print(f"XML content has been saved to {output_file_path}") """
    

from csv_to_xml_converter import CSVtoXMLConverter
from lxml import etree

if __name__ == "__main__":
    # Caminho do arquivo CSV
    csv_file_path = "/data/Electric_Vehicle_Population_Data.csv"

    # Caminho do esquema XML
    schema_file_path = "/data/schema.xsd"

    # Instanciar o conversor CSV para XML
    converter = CSVtoXMLConverter(csv_file_path)

    # Obter a string XML
    xml_content = converter.to_xml_str()

    # Validar o XML em relação ao schema
    schema = etree.XMLSchema(file=schema_file_path)
    parser = etree.XMLParser(schema=schema)

    try:
        # Tenta analisar o XML
        root = etree.fromstring(xml_content, parser)
        print("O XML está em conformidade com o esquema.")
        
        # Caminho do arquivo de saída XML
        output_file_path = "/data/output.xml"

        # Salvar o conteúdo XML no arquivo de saída
        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write(xml_content)

        print(f"O conteúdo XML foi salvo em {output_file_path}")

    except etree.DocumentInvalid as e:
        # Se houver um erro de validação, imprima o erro
        print(f"Erro de validação do esquema: {e}")
        for error in schema.error_log:
            print(f"Erro: {error.message}, Linha: {error.line}, Coluna: {error.column}")
