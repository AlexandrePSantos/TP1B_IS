import csv
import xml.dom.minidom as md
import xml.etree.ElementTree as ET
from csv_reader import CSVReader

# Importando classes do módulo entities.sample
from entities.sample.country import Country
from entities.sample.team import Team
from entities.sample.player import Player

# Importando classes do módulo entities
from entities.car import *
from entities.cafv import *
from entities.location import *
from entities.utility import *


class CSVtoXMLConverter:

    def __init__(self, path):
        # Inicializando o leitor de CSV com o caminho fornecido
        self._reader = CSVReader(path)

    def to_xml(self):
        # Ler informações sobre países
        countries = self._reader.read_entities(
            attr="nationality",
            builder=lambda row: Country(row["nationality"])
        )
        
        states = self._reader.read_entities(
            attr="state",
            builder=lambda row: State(row["state"]),
        )
        
        cities = self._reader.read_entities(
            attr="city",
            builder=lambda row: City(row["city"]),
            after_create=states[]
            #adicionar a cidade perguntar diogo que ele ja nao sabia o que fazer
        )

        # Ler informações sobre equipas (times)
        teams = self._reader.read_entities(
            attr="Current Club",
            builder=lambda row: Team(row["Current Club"])
        )

        # Ler informações sobre jogadores
        def after_creating_player(player, row):
            # Adicionar o jogador à equipa apropriada
            teams[row["Current Club"]].add_player(player)

        self._reader.read_entities(
            attr="full_name",
            builder=lambda row: Player(
                name=row["full_name"],
                age=row["age"],
                country=countries[row["nationality"]]
            ),
            after_create=after_creating_player
        )

        # Gerar o XML final
        root_el = ET.Element("EletricCars")

        # Elemento para armazenar informações sobre as equipas
        teams_el = ET.Element("Teams")
        for team in teams.values():
            teams_el.append(team.to_xml())

        # Elemento para armazenar informações sobre os países
        countries_el = ET.Element("Countries")
        for country in countries.values():
            countries_el.append(country.to_xml())

        # Adicionar elementos ao elemento raiz
        root_el.append(teams_el)
        root_el.append(countries_el)

        return root_el

    def to_xml_str(self):
        # Converter a estrutura XML para uma string formatada
        xml_str = ET.tostring(
            self.to_xml(), encoding='utf8', method='xml').decode()
        dom = md.parseString(xml_str)
        return dom.toprettyxml()
