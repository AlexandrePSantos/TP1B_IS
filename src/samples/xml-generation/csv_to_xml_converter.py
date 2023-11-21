import csv
import xml.dom.minidom as md
import xml.etree.ElementTree as ET
from csv_reader import CSVReader

# Importando classes do módulo entities
from entities.cafv import Cafv
from entities.utility import Utility


class CSVtoXMLConverter:

    def __init__(self, path):
        self._reader = CSVReader(path)

    def to_xml(self):
        # Read cafv
        cafv_collection = self._reader.read_entities(
            attr="CAFV Eligibility",
            builder=lambda row: Cafv(row["CAFV Eligibility"])
        )

        # Read electric utilities
        electric_utilities_collection = self._reader.read_entities(
            attr="Electric Utility",
            builder=lambda row: Utility(row["Electric Utility"])
        )

        # Generate the final XML
        root_el = ET.Element("ElectricCars")

        cafv_eligibility_el = ET.Element("CAFVEligibility")
        for cafv in cafv_collection.values():
            cafv_eligibility_el.append(cafv.to_xml())
            
        electric_utilities_el = ET.Element("ElectricUtility")
        for elut in electric_utilities_collection.values():
            electric_utilities_el.append(elut.to_xml())
        
        # root_el.append(makers_el)
        root_el.append(cafv_eligibility_el)
        root_el.append(electric_utilities_el)
        
        return root_el

    def to_xml_str(self):
        # Converter a estrutura XML para uma string formatada
        xml_str = ET.tostring(
            self.to_xml(), encoding='utf8', method='xml').decode()
        dom = md.parseString(xml_str)
        return dom.toprettyxml()
