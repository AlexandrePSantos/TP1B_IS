import xml.etree.ElementTree as ET

class Model:

    def __init__(self, name, etype):
        Model.counter += 1
        self._id = Model.counter
        self._name = name
        self._etype = etype

    def to_xml(self):
        el = ET.Element("Model")  # Criando um elemento XML para representar o utilitário
        el.set("id", str(self._id))  # Atribuindo atributos ID e name ao elemento
        el.set("name", self._name)
        el.set("eletric type", self._etype)
        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"name: {self._name}, id:{self._id}, eletric type:{self._etype}"

Model.counter = 0