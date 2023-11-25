import xml.etree.ElementTree as ET
from entities.city import City

class State:

    def __init__(self, name):
        State.counter += 1
        self._id = State.counter
        self._name = name
        self._cities = []
        
    def add_city(self, city: City):
        self._cities.append(city)

    def to_xml(self):
        el = ET.Element("State")  # Criando um elemento XML para representar o utilitário
        el.set("id", str(self._id))  # Atribuindo atributos ID e name ao elemento
        el.set("name", self._name)
        
        for city in self._cities:
            el.append(city.to_xml())
        
        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"name: {self._name}, id:{self._id}"

State.counter = 0
