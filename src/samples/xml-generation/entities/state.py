# Price, Mileage, Assembly, Registration Status
import xml.etree.ElementTree as ET


class State:

    def __init__(self, name):
        State.counter += 1
        self._id = State.counter
        self._name = name
            
    # def to_xml(self):
    #     el = ET.Element("Country")
    #     el.set("id", str(self._id))
    #     el.set("name", self._name)
    #     return el

    # def get_id(self):
    #     return self._id

    # def __str__(self):
    #     return f"name: {self._name}, id:{self._id}"
    
State.counter = 0
