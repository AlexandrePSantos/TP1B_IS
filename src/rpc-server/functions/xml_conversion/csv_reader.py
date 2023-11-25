from csv import DictReader

# Definindo a classe CSVReader
class CSVReader:

    # Inicializador da classe
    def __init__(self, path, delimiter=','):
        # Caminho do arquivo CSV
        self._path = path
        # Delimitador utilizado no arquivo CSV (padrão é a vírgula)
        self._delimiter = delimiter

    # Método para iterar sobre as linhas do arquivo CSV
    def loop(self):
        with open(self._path, 'r') as file:
            for row in DictReader(file, delimiter=self._delimiter):
                yield row
        # Garante que o arquivo seja fechado após a leitura
        file.close()

    # Método para ler entidades do arquivo CSV e construir objetos com base em um atributo específico
    def read_entities(self, attr, builder, after_create=None):
        entities = {}

        # Itera sobre as linhas do arquivo
        for row in self.loop():
            e = row[attr]
            # Se a entidade ainda não estiver presente no dicionário, cria um objeto usando o construtor
            if e not in entities:
                entities[e] = builder(row)
                # Executa uma função após a criação do objeto, se fornecida
                after_create is not None and after_create(entities[e], row)

        return entities

