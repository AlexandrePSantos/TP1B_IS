import csv
import xml.dom.minidom as md
import xml.etree.ElementTree as ET
from csv_reader import CSVReader

# Importando classes do módulo entities
from entities.maker import Maker
from entities.maker import Model
from entities.model import Car
from entities.state import State
from entities.state import City
from entities.cafv import Cafv
from entities.utility import Utility


class CSVtoXMLConverter:

    def __init__(self, path):
        self._reader = CSVReader(path)

    def to_xml(self):
        # Read maker
        maker_collection = self._reader.read_entities(
            attr="Maker",
            builder=lambda row: Maker(row["Maker"])
        )
        
        state_collection = self._reader.read_entities(
            attr="State",
            builder=lambda row: State(row["State"])
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
        
        # LOCATION COLUMNS
        def after_creating_city(city, row):
                # add the model to the appropriate team
                state_collection[row["State"]].add_city(city)

        city_collection = self._reader.read_entities(
            attr="City",
            builder=lambda row: City(
                name=row["City"]
            ),
            after_create=after_creating_city
        )

        # CAR COLUMNS
        def after_creating_model(model, row):
                # add the model to the appropriate team
                maker_collection[row["Maker"]].add_model(model)

        model_collection = self._reader.read_entities(
            attr="Model",
            builder=lambda row: Model(
                name=row["Model"],
                etype=row["Electric Type"]
            ),
            after_create=after_creating_model
        )

        def after_creating_car(car, row):
                # add the model to the appropriate team
                model_collection[row["Model"]].add_car(car)

        self._reader.read_entities(
            attr="DOL Vehicle ID",
            builder=lambda row: Car(
                dol=row["DOL Vehicle ID"],
                vin=row["VIN"],
                modyear=row["Model Year"],
                erange=row["Electric Range"],
                cafv=cafv_collection[row["CAFV Eligibility"]],
                utility=electric_utilities_collection[row["Electric Utility"]],
                city=city_collection[row["City"]]
            ),
            after_create=after_creating_car
        )

        # Generate the final XML
        root_el = ET.Element("ElectricCars")

        makers_el = ET.Element("Makers")
        for maker in maker_collection.values():
            makers_el.append(maker.to_xml())
            
        state_el = ET.Element("Locations")
        for state in state_collection.values():
            state_el.append(state.to_xml())
            
        cafv_eligibility_el = ET.Element("CAFVEligibility")
        for cafv in cafv_collection.values():
            cafv_eligibility_el.append(cafv.to_xml())
            
        electric_utilities_el = ET.Element("ElectricUtility")
        for elut in electric_utilities_collection.values():
            electric_utilities_el.append(elut.to_xml())
        
        root_el.append(makers_el)
        root_el.append(state_el)
        root_el.append(cafv_eligibility_el)
        root_el.append(electric_utilities_el)
        
        return root_el

    def to_xml_str(self):
        # Converter a estrutura XML para uma string formatada
        xml_str = ET.tostring(
            self.to_xml(), encoding='utf8', method='xml').decode()
        dom = md.parseString(xml_str)
        return dom.toprettyxml()
