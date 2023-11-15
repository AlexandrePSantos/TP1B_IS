import xml.etree.ElementTree as ET

# Definindo a classe Player
class Player:

    # Inicializador da classe
    def __init__(self, name, age, country):
        # Incrementa o contador de instâncias de Player
        Player.counter += 1
        # Atribui um ID único baseado no contador
        self._id = Player.counter
        # Atribui o nome do jogador
        self._name = name
        # Atribui a idade do jogador
        self._age = age
        # Atribui o país do jogador (assumindo que seja uma instância da classe Country)
        self._country = country

    # Método para gerar um elemento XML representando o jogador
    def to_xml(self):
        el = ET.Element("Player")
        el.set("id", str(self._id))
        el.set("name", self._name)
        el.set("age", str(self._age))  # Converte a idade para string
        el.set("country_ref", str(self._country.get_id()))  # Obtém o ID do país associado ao jogador
        return el

    # Método especial para representação em string do objeto Player
    def __str__(self):
        return f"{self._name}, age:{self._age}, country:{self._country}"

# Inicializando o contador de instâncias de Player
Player.counter = 0