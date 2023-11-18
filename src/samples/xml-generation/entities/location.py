import xml.etree.ElementTree as ET

class Location:

    counter = 0

    def __init__(self, name):
        Location.counter += 1
        self._id = Location.counter
        self._name = name
        self._states = []

    def add_state(self, state_name):
        state = State(state_name)
        self._states.append(state)
        return state

    def to_xml(self):
        root_el = ET.Element("Locations")  # Use a root element (you can name it as per your preference)

        for state in self._states:
            root_el.append(state.to_xml())  # Directly append the state XML representation to the root element

        return root_el

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def __str__(self):
        return f"name: {self._name}, id:{self._id}"

class State:

    state_counter = 0

    def __init__(self, name):
        State.state_counter += 1
        self._id = State.state_counter
        self._name = name
        self._cities = []

    def add_city(self, city_name):
        city = City(city_name)
        self._cities.append(city)
        return city

    def to_xml(self):
        state_el = ET.Element("State", id=str(self._id), name=self._name)

        for city in self._cities:
            state_el.append(city.to_xml())  # Directly append the city XML representation to the state element

        return state_el

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

class City:

    city_counter = 0

    def __init__(self, name):
        City.city_counter += 1
        self._id = City.city_counter
        self._name = name
        self._counties = []

    def add_county(self, county_name):
        county = County(county_name)
        self._counties.append(county)
        return county

    def to_xml(self):
        city_el = ET.Element("City", id=str(self._id), name=self._name)

        for county in self._counties:
            city_el.append(county.to_xml())  # Directly append the county XML representation to the city element

        return city_el

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

class County:

    county_counter = 0

    def __init__(self, name):
        County.county_counter += 1
        self._id = County.county_counter
        self._name = name

    def to_xml(self):
        county_el = ET.Element("County", id=str(self._id), name=self._name)
        return county_el

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name
