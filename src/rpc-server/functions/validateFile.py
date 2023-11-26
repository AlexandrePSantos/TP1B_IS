from lxml import etree

def validate(xml_path: str, xsd_path: str) -> bool:
    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    xml_doc = etree.parse(xml_path)
    result = xmlschema.validate(xml_doc)

    return result


def validateFile() -> str:
    xml_path = '/data/result.xml'
    xsd_path = '/data/schema.xsd'

    if validate(xml_path, xsd_path):
        return "\nThe XML file is valid"
    else:
        return "\nThe XML file is not valid"
