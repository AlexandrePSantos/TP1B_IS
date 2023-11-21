import xml.etree.ElementTree as ET
from entities.county import County

class City:

    def __init__(self, name):
        City.counter += 1
        self._id = City.counter
        self._name = name
        self._counties = []
        
    def add_counties(self, county: County):
        self._counties.append(county)

    def to_xml(self):
        el = ET.Element("City")  # Criando um elemento XML para representar o utilitário
        el.set("id", str(self._id))  # Atribuindo atributos ID e name ao elemento
        el.set("name", self._name)
        
        counties_el = ET.Element("County")
        for county in self._counties:
            counties_el.append(county.to_xml())

        el.append(counties_el)
        
        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"name: {self._name}, id:{self._id}"

City.counter = 0
