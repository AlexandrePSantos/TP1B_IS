import sys
import os

# Adiciona o diretório ao caminho do sistema
module_path = os.path.join('/app', 'validate_xml.py')
sys.path.append('/app')

# Importa diretamente a função do módulo
# from validate_xml import verifica_xml

# def loadToDB():
#     # Chama a função verifica_xml diretamente
#     verifica_xml()
    
def remove():
    print("Função para remover o xml da bd!")
