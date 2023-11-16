# VIN, Maker, Model, Eletric Type, Model Year, Eletric Range
# Reference: CAFV, Utility, Location
import xml.etree.ElementTree as ET


class Car:

    def __init__(self, company, model, city):
        Car.counter += 1
        self._id = Car.counter
        self._company = company
        self._model = model
        self._city = city
            
    def to_xml(self):
        el = ET.Element("Car")
        el.set("id", str(self._id))
        el.set("name", self._name)
        el.set("age", self._age)
        el.set("location_ref", str(self._city.get_id()))
        return el

    def __str__(self):
        return f"{self._company}, age:{self._model}, country:{self._city}"
    
Car.counter = 0

class Car:

    def __init__(self, company, model, city):
        Car.counter += 1
        self._id = Car.counter
        self._company = company
        self._model = model
        self._city = city
            
    def to_xml(self):
        el = ET.Element("Car")
        el.set("id", str(self._id))
        el.set("name", self._name)
        el.set("age", self._age)
        el.set("location_ref", str(self._city.get_id()))
        return el

    def __str__(self):
        return f"{self._company}, age:{self._model}, country:{self._city}"
    
Car.counter = 0
