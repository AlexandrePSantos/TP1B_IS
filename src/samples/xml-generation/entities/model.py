import xml.etree.ElementTree as ET
from entities.car import Car

class Model:

    def __init__(self, name):
        Model.counter += 1
        self._id = Model.counter
        self._name = name
        self._cars = []
        
    def add_car(self, car: Car):
        self._cars.append(car)

    def to_xml(self):
        el = ET.Element("Model")  # Criando um elemento XML para representar o utilitário
        el.set("id", str(self._id))  # Atribuindo atributos ID e name ao elemento
        el.set("name", self._name)
        
        cars_el = ET.Element("Car")
        for car in self._cars:
            cars_el.append(car.to_xml())

        el.append(cars_el)
        
        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"name: {self._name}, id:{self._id}"

Model.counter = 0
