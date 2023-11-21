import xml.etree.ElementTree as ET
from entities.model import Model

class Maker:

    def __init__(self, name):
        Maker.counter += 1
        self._id = Maker.counter
        self._name = name
        self._models = []
        
    def add_model(self, model: Model):
        self._models.append(model)

    def to_xml(self):
        el = ET.Element("Maker")  # Criando um elemento XML para representar o utilitário
        el.set("id", str(self._id))  # Atribuindo atributos ID e name ao elemento
        el.set("name", self._name)
        
        models_el = ET.Element("Model")
        for model in self._models:
            models_el.append(model.to_xml())

        el.append(models_el)
        
        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"name: {self._name}, id:{self._id}"

Maker.counter = 0
