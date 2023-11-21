import xml.etree.ElementTree as ET

class Car:
    
    def __init__(self, vin):
        Car.counter += 1
        self._id = Car.counter
        self._vin = vin
        # self._county = county
        # self._model = model
        # self._modyear = modyear
        # self._range = erange

    def to_xml(self):
        el = ET.Element("Car")  # Criando um elemento XML para representar o utilitário
        el.set("id", str(self._id))  # Atribuindo atributos ID e name ao elemento
        el.set("VIN", self._vin)
        # el.set("county_ref", str(self._county.get_id()))
        # el.set("Model", self._model)
        # el.set("Model year", str(self._modyear))
        # el.set("Electric Range", str(self._range))
        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"VIN: {self._name}, id:{self._id}"

Car.counter = 0