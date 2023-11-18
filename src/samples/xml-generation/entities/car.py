# VIN, Maker, Model, Eletric Type, Model Year, Eletric Range
# Reference: CAFV, Utility, Location
import xml.etree.ElementTree as ET

class CarCollection:

    def __init__(self):
        self._makers = []

    def add_maker(self, maker_name):
        maker = Maker(maker_name)
        self._makers.append(maker)
        return maker

    def to_xml(self):
        makers_el = ET.Element("Makers")

        for maker in self._makers:
            makers_el.append(maker.to_xml())

        return makers_el

class Maker:

    counter = 0

    def __init__(self, name):
        Maker.counter += 1
        self._id = Maker.counter
        self._name = name
        self._models = []

    def add_model(self, model_name, electric_type):
        model = Model(model_name, electric_type)
        self._models.append(model)
        return model

    def to_xml(self):
        maker_el = ET.Element("Maker")
        maker_el.set("id", str(self._id))
        maker_el.set("name", self._name)

        for model in self._models:
            maker_el.append(model.to_xml())

        return maker_el

class Model:

    counter = 0

    def __init__(self, name, electric_type):
        Model.counter += 1
        self._id = Model.counter
        self._name = name
        self._electric_type = electric_type
        self._cars = []

    def add_car(self, vin, model_year, electric_range, cafv_ref, utility_ref, county_ref):
        car = Car(vin, model_year, electric_range, cafv_ref, utility_ref, county_ref)
        self._cars.append(car)
        return car

    def to_xml(self):
        model_el = ET.Element("Model")
        model_el.set("id", str(self._id))
        model_el.set("name", self._name)
        model_el.set("Electric_Type", self._electric_type)

        for car in self._cars:
            model_el.append(car.to_xml())

        return model_el

class Car:

    counter = 0

    def __init__(self, vin, model_year, electric_range, cafv_ref, utility_ref, county_ref):
        Car.counter += 1
        self._id = Car.counter
        self._vin = vin
        self._model_year = model_year
        self._electric_range = electric_range
        self._cafv_ref = cafv_ref
        self._utility_ref = utility_ref
        self._county_ref = county_ref

    def to_xml(self):
        car_el = ET.Element("Car")
        car_el.set("VIN", self._vin)
        car_el.set("modelyear", str(self._model_year))
        car_el.set("electricrange", str(self._electric_range))
        car_el.set("cafv_ref", str(self._cafv_ref))
        car_el.set("utility_ref", str(self._utility_ref))
        car_el.set("county_ref", str(self._county_ref))
        return car_el
    