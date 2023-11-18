import xml.etree.ElementTree as ET

# Definindo a classe CafvEligibilityCollection
class CafvEligibilityCollection:

    def __init__(self):
        self._eligibilities = []  # Lista para armazenar instâncias da classe CafvEligibility

    def add_eligibility(self, eligibility_name):
        eligibility = CafvEligibility(eligibility_name)
        self._eligibilities.append(eligibility)
        return eligibility

    def to_xml(self):
        cafv_eligibilities_el = ET.Element("CAFV Eligibility")  # Elemento raiz XML

        # Adicionando os elementos XML das elegibilidades à coleção
        for eligibility in self._eligibilities:
            cafv_eligibilities_el.append(eligibility.to_xml())

        return cafv_eligibilities_el

# Definindo a classe CafvEligibility
class CafvEligibility:

    # Variável de classe para manter um contador global de elegibilidades criadas
    counter = 0

    def __init__(self, name):
        CafvEligibility.counter += 1
        self._id = CafvEligibility.counter
        self._name = name

    def to_xml(self):
        el = ET.Element("Eligibility")  # Criando um elemento XML para representar a elegibilidade
        el.set("id", str(self._id))  # Atribuindo atributos ID e name ao elemento
        el.set("name", self._name)
        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"name: {self._name}, id:{self._id}"
