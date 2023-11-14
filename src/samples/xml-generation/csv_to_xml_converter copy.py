import csv
import xml.dom.minidom as md
import xml.etree.ElementTree as ET
from csv_reader import CSVReader

# Main CSV
from entities.car import Car
from entities.location import Location
from entities.utility import Utility
from entities.cafv import Cafv

class CSVtoXMLConverter:

    def __init__(self, path):
        self._reader = CSVReader(path)

    def to_xml(self):   
        # read car
        # read location
        # read utility
        # read cafv
        cafvs = self._reader.read_entities(
            attr="Clean Alternative Fuel Vehicle (CAFV) Eligibility",
            builder=lambda row: Cafv(row["Clean Alternative Fuel Vehicle (CAFV) Eligibility"])
        )


        # generate the final xml

    def to_xml_str(self):
        xml_str = ET.tostring(self.to_xml(), encoding='utf8', method='xml').decode()
        dom = md.parseString(xml_str)
        return dom.toprettyxml()
