import importlib.util

# Specify the absolute path to the module
module_path = 'src/samples/xml-generation/validate_xml.py'

# Create a spec from the path
spec = importlib.util.spec_from_file_location('validate_xml.py', module_path)

# Import the module
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def validate():
    module.verifica_xml()

def loadToDB():
    print("Função para carregar o xml para a bd!")

def remove():
    print("Função para remover o xml da bd!")
