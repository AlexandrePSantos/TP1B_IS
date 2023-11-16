# CAFV Eligibility
import xml.etree.ElementTree as ET


class Cafv:

    def __init__(self, name):
        Cafv.counter += 1
        self._id = Cafv.counter
        self._name = name
            
    def to_xml(self):
        el = ET.Element("Clean Alternative Fuel Vehicle (CAFV) Eligibility")
        el.set("id", str(self._id))
        el.set("name", self._name)
        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"name: {self._name}, id:{self._id}"
    
Cafv.counter = 0