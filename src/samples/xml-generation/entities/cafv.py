# CAFV Eligibility
import xml.etree.ElementTree as ET

class CafvEligibilityCollection:

    def __init__(self):
        self._eligibilities = []

    def add_eligibility(self, eligibility_name):
        eligibility = CafvEligibility(eligibility_name)
        self._eligibilities.append(eligibility)
        return eligibility

    def to_xml(self):
        cafv_eligibilities_el = ET.Element("CAFV Eligibility")

        for eligibility in self._eligibilities:
            cafv_eligibilities_el.append(eligibility.to_xml())

        return cafv_eligibilities_el

class CafvEligibility:

    counter = 0

    def __init__(self, name):
        CafvEligibility.counter += 1
        self._id = CafvEligibility.counter
        self._name = name

    def to_xml(self):
        el = ET.Element("Eligibility")
        el.set("id", str(self._id))
        el.set("name", self._name)
        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"name: {self._name}, id:{self._id}"
    