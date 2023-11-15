import xml.etree.ElementTree as ET

# Definindo a classe Country
class Country:

    # Inicializador da classe
    def __init__(self, name):
        # Incrementa o contador de instâncias de Country
        Country.counter += 1
        # Atribui um ID único baseado no contador
        self._id = Country.counter
        # Atribui o nome do país
        self._name = name

    # Método para gerar um elemento XML representando o país
    def to_xml(self):
        el = ET.Element("Country")
        el.set("id", str(self._id))
        el.set("name", self._name)
        return el

    # Método para obter o ID do país
    def get_id(self):
        return self._id

    # Método especial para representação em string do objeto Country
    def __str__(self):
        return f"name: {self._name}, id:{self._id}"

# Inicializando o contador de instâncias de Country
Country.counter = 0