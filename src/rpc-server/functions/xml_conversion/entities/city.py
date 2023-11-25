import xml.etree.ElementTree as ET

class City:

    def __init__(self, name):
        City.counter += 1
        self._id = City.counter
        self._name = name
        
    def to_xml(self):
        el = ET.Element("City")  # Criando um elemento XML para representar o utilitário
        el.set("id", str(self._id))  # Atribuindo atributos ID e name ao elemento
        el.set("name", self._name)
        
        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"name: {self._name}, id:{self._id}"

City.counter = 0
