import xml.etree.ElementTree as ET

def verifica_xml(xml_string):
    try:
        # Tenta analisar o XML
        root = ET.fromstring(xml_string)
        print("XML está bem formado.")
        return True
    except ET.ParseError as e:
        print(f"Erro ao analisar o XML: {e}")
        return False

def verificar_arquivo_xml(caminho_do_arquivo):
    try:
        # Lê o conteúdo do arquivo XML
        with open(caminho_do_arquivo, 'r') as arquivo:
            xml_string = arquivo.read()

        # Verifica se o XML é bem formado
        return verifica_xml(xml_string)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_do_arquivo}")
        return False

# Exemplo de uso
caminho_do_arquivo_xml = 'caminho/do/seu/arquivo.xml'

if verificar_arquivo_xml(caminho_do_arquivo_xml):
    # Faça algo se o XML estiver bem formado
    print("Fazer algo com o XML...")
else:
    # Trate caso haja erros no XML
    print("Corrija os erros no XML antes de prosseguir.")