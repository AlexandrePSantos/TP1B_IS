import xml.etree.ElementTree as ET

class Car:
    
    def __init__(self, vin, modyear, erange, cafv, utility, city):
        Car.counter += 1
        self._id = Car.counter
        self._vin = vin
        self._modyear = modyear
        self._erange = erange
        self._cafv = cafv
        self._utility = utility
        self._city = city

    def to_xml(self):
        el = ET.Element("Car")  # Criando um elemento XML para representar o utilitário
        el.set("id", str(self._id))  # Atribuindo atributos ID e name ao elemento
        el.set("VIN", self._vin)
        el.set("year", str(self._modyear))
        el.set("range", str(self._erange))
        el.set("cafv_ref", str(self._cafv.get_id())) 
        el.set("utility_ref", str(self._utility.get_id()))
        el.set("city_ref", str(self._city.get_id())) 
        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"VIN: {self._name}, id:{self._id}, model year:{self._modyear}, electric range:{self._erange}, cafv_ref:{self._cafv}, utility_ref:{self._utility}, city_ref:{self._county}"

Car.counter = 0