import csv
import xml.dom.minidom as md
import xml.etree.ElementTree as ET
from csv_reader import CSVReader

# Importando classes do módulo entities
from entities.car import *
from entities.cafv import *
from entities.location import *
from entities.utility import *


class CSVtoXMLConverter:

    def __init__(self, path):
        self._reader = CSVReader(path)

    def to_xml(self):
        # Read locations
        locations = self._reader.read_entities(
            attr="Location",
            builder=lambda row: Location(row["Location"])
        )

        # Read cafv
        cafv_collection = self._reader.read_entities(
            attr="CAFV Eligibility",
            builder=lambda row: Cafv(row["CAFV Eligibility"])
        )

        # Read electric utilities
        electric_utilities_collection = self._reader.read_entities(
            attr="Electric Utility",
            builder=lambda row: Utility(row["Electric Utility"])
        )

        # Read cars
        def after_creating_car(car, row):
            # Assign references to location, cafv, and utility
            car.set_location(locations[row["Location"]])
            car.set_cafv(cafv_collection[row["CAFV Eligibility"]])
            car.set_utility(electric_utilities_collection[row["Electric Utility"]])

        cars = self._reader.read_entities(
            attr="VIN",
            builder=lambda row: Car(
                vin=row["VIN"],
                maker=row["Maker"],
                model=row["Model"],
                electric_type=row["Electric Type"],
                model_year=row["Model Year"],
                electric_range=row["Electric Range"]
            ),
            after_create=after_creating_car
        )

        # Generate the final XML
        root_el = ET.Element("ElectricCars")

        makers_el = ET.Element("Makers")
        for maker in set(car.maker for car in cars.values()):
            maker_el = ET.Element("Maker", id=str(len(makers_el)), name=maker)
            models_el = ET.Element("Models")

            for model in set(car.model for car in cars.values() if car.maker == maker):
                model_el = ET.Element("Model", id=str(len(models_el)), name=model, Electric_Type="BEV")  # Assuming Electric_Type is constant for now
                cars_el = ET.Element("Cars")

                for car in cars.values():
                    if car.maker == maker and car.model == model:
                        car_el = car.to_xml()
                        cars_el.append(car_el)

                model_el.append(cars_el)
                models_el.append(model_el)

            maker_el.append(models_el)
            makers_el.append(maker_el)

        cafv_eligibility_el = cafv_collection.to_xml()
        electric_utilities_el = electric_utilities_collection.to_xml()
        locations_el = ET.Element("Locations")

        for location in locations.values():
            locations_el.append(location.to_xml())

        root_el.append(makers_el)
        root_el.append(cafv_eligibility_el)
        root_el.append(electric_utilities_el)
        root_el.append(locations_el)

        return root_el

    def to_xml_str(self):
        # Converter a estrutura XML para uma string formatada
        xml_str = ET.tostring(
            self.to_xml(), encoding='utf8', method='xml').decode()
        dom = md.parseString(xml_str)
        return dom.toprettyxml()
