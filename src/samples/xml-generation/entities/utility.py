import xml.etree.ElementTree as ET

# Definindo a classe ElectricUtilitiesCollection
class ElectricUtilitiesCollection:

    def __init__(self):
        self._utilities = []  # Lista para armazenar instâncias da classe Utility

    def add_utility(self, utility_name):
        utility = Utility(utility_name)
        self._utilities.append(utility)
        return utility

    def to_xml(self):
        utilities_el = ET.Element("ElectricUtilities")  # Elemento raiz XML

        # Adicionando os elementos XML dos utilitários à coleção
        for utility in self._utilities:
            utilities_el.append(utility.to_xml())

        return utilities_el

# Definindo a classe Utility
class Utility:

    # Variável de classe para manter um contador global de utilitários criados
    counter = 0

    def __init__(self, name):
        Utility.counter += 1
        self._id = Utility.counter
        self._name = name

    def to_xml(self):
        el = ET.Element("Utility")  # Criando um elemento XML para representar o utilitário
        el.set("id", str(self._id))  # Atribuindo atributos ID e name ao elemento
        el.set("name", self._name)
        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"name: {self._name}, id:{self._id}"
