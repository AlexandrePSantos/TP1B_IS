import xml.etree.ElementTree as ET

# Definindo a classe CafvEligibility
class Cafv:

    def __init__(self, name):
        Cafv.counter += 1
        self._id = Cafv.counter
        self._name = name

    def to_xml(self):
        el = ET.Element("Eligibility")  # Criando um elemento XML para representar a elegibilidade
        el.set("id", str(self._id))  # Atribuindo atributos ID e name ao elemento
        el.set("name", self._name)
        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"name: {self._name}, id:{self._id}"

Cafv.counter = 0
