import psycopg2
import os
from functions.xml.validate_xml import Validation
from functions.db.db import Database

# Converte csv para xml e valida o formato
def convert():
    Validation.verifica_xml()

# Carrega XML para a BD    
def loadToDB():
    Database.load()

# Lista ficheiros na BD
def listFiles():
    Database.list()
  
# Remove ficheiro da BD (id do ficheiro na tabela)
def removeFiles(id):
    Database.remove(id)
