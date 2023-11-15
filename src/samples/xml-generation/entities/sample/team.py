import xml.etree.ElementTree as ET
from entities.sample.player import Player  # Certifique-se de que o caminho do módulo está correto

# Definindo a classe Team
class Team:

    # Inicializador da classe
    def __init__(self, name: str):
        # Incrementa o contador de instâncias de Team
        Team.counter += 1
        # Atribui um ID único baseado no contador
        self._id = Team.counter
        # Atribui o nome da equipa
        self._name = name
        # Inicializa a lista de jogadores
        self._players = []

    # Método para adicionar um jogador à equipa
    def add_player(self, player: Player):
        self._players.append(player)

    # Método para gerar um elemento XML representando a equipa
    def to_xml(self):
        el = ET.Element("Team")
        el.set("id", str(self._id))
        el.set("name", self._name)

        # Cria um elemento XML para os jogadores da equipa
        players_el = ET.Element("Players")
        for player in self._players:
            players_el.append(player.to_xml())

        # Adiciona o elemento dos jogadores ao elemento da equipa
        el.append(players_el)

        return el

    # Método especial para representação em string do objeto Team
    def __str__(self):
        return f"{self._name} ({self._id})"

# Inicializando o contador de instâncias de Team
Team.counter = 0