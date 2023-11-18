import xml.etree.ElementTree as ET

# Definindo a classe Location
class Location:

    # Variável de classe para manter um contador global de localizações criadas
    counter = 0

    # Método de inicialização da classe
    def __init__(self, name):
        Location.counter += 1
        self._id = Location.counter
        self._name = name
        self._states = []  # Lista para armazenar instâncias da classe State

    # Método para adicionar um estado à localização
    def add_state(self, state_name):
        state = State(state_name)
        self._states.append(state)
        return state

    # Método para converter a localização para XML
    def to_xml(self):
        location_el = ET.Element("Location", id=str(self._id), name=self._name)

        # Adicionando os elementos XML dos estados à localização
        for state in self._states:
            location_el.append(state.to_xml())

        return location_el

    # Métodos para obter o ID e o nome da localização
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    # Método de representação em string da localização
    def __str__(self):
        return f"name: {self._name}, id:{self._id}"

# Definindo a classe State
class State:

    # Variável de classe para manter um contador global de estados criados
    state_counter = 0

    # Método de inicialização da classe
    def __init__(self, name):
        State.state_counter += 1
        self._id = State.state_counter
        self._name = name
        self._cities = []  # Lista para armazenar instâncias da classe City

    # Método para adicionar uma cidade ao estado
    def add_city(self, city_name):
        city = City(city_name)
        self._cities.append(city)
        return city

    # Método para converter o estado para XML
    def to_xml(self):
        state_el = ET.Element("State", id=str(self._id), name=self._name)

        # Adicionando os elementos XML das cidades ao estado
        for city in self._cities:
            state_el.append(city.to_xml())

        return state_el

    # Métodos para obter o ID e o nome do estado
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

# Definindo a classe City
class City:

    # Variável de classe para manter um contador global de cidades criadas
    city_counter = 0

    # Método de inicialização da classe
    def __init__(self, name):
        City.city_counter += 1
        self._id = City.city_counter
        self._name = name
        self._counties = []  # Lista para armazenar instâncias da classe County

    # Método para adicionar um condado à cidade
    def add_county(self, county_name):
        county = County(county_name)
        self._counties.append(county)
        return county

    # Método para converter a cidade para XML
    def to_xml(self):
        city_el = ET.Element("City", id=str(self._id), name=self._name)

        # Adicionando os elementos XML dos condados à cidade
        for county in self._counties:
            city_el.append(county.to_xml())

        return city_el

    # Métodos para obter o ID e o nome da cidade
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

# Definindo a classe County
class County:

    # Variável de classe para manter um contador global de condados criados
    county_counter = 0

    # Método de inicialização da classe
    def __init__(self, name):
        County.county_counter += 1
        self._id = County.county_counter
        self._name = name

    # Método para converter o condado para XML
    def to_xml(self):
        county_el = ET.Element("County", id=str(self._id), name=self._name)
        return county_el

    # Métodos para obter o ID e o nome do condado
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name
