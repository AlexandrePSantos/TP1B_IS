#   State, City, County 
import xml.etree.ElementTree as ET


# Estados (1)
class State:
    _city = []

    def __init__(self, name):
        State.counter += 1
        self._id = State.counter
        self._name = name
            
    def add_city(self, city):
        self._city.append(city.get_id())
            
    def get_id(self):
        return self._id
            
    def to_xml(self):
        el = ET.Element("State")
        el.set("id", str(self._id))
        el.set("name", self._name)
        return el

    def __str__(self):
        return f"{self._name}"
    
State.counter = 0


# Cidades (2)
class City:
    _county = []
    
    def __init__(self, name):
        City.counter += 1
        self._id = City.counter
        self._name = name
        
    def add_county(self, county):
        self._county.append(county.get_id())
            
    def get_id(self):
        return self._id
            
    def to_xml(self):
        el = ET.Element("City")
        el.set("id", str(self._id))
        el.set("name", self._name)
        return el

    def __str__(self):
        return f"{self._name}"
    
City.counter = 0


# Vila (3)
class County:

    def __init__(self, name):
        County.counter += 1
        self._id = County.counter
        self._name = name
            
    def get_id(self):
        return self._id
            
    def to_xml(self):
        el = ET.Element("County")
        el.set("id", str(self._id))
        el.set("name", self._name)
        return el

    def __str__(self):
        return f"{self._name}"
    
County.counter = 0
    