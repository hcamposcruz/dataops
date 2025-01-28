import csv
from database_connection import DatabaseConnection

class DataImporter:
    def __init__(self, db_config):
        self.db_config = db_config
        self.db = None

    def connect_to_db(self):
        self.db = DatabaseConnection(
            host=self.db_config['host'],
            port=int(self.db_config['port']),
            user=self.db_config['user'],
            password=self.db_config['password']
        )
        self.connection = self.db.connect()

    def clean_data(self, row):
        # Limpeza básica dos dados
        row['nome cliente'] = row['nome cliente'].strip().title()
        row['endereco'] = row['endereco'].strip().title()
        row['cidade'] = row['cidade'].strip().title()
        row['CEP'] = row['CEP'].strip()
        row['codigo_produto'] = int(row['codigo_produto'])
        row['nome produto'] = row['nome produto'].strip().title()
        row['valor_produto'] = float(row['valor_produto'])
        row['quantidade_comprada'] = int(row['quantidade_comprada'])
        row['valor_total_compra'] = float(row['valor_total_compra'])
        return row

    def import_data_from_csv(self, csv_file):
        self.connect_to_db()
        cursor = self.connection.cursor()
        
        with open(csv_file, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=';')
            for row in csv_reader:
                row = self.clean_data(row)
                cursor.execute("""
                    INSERT INTO dados.importacao (nome_cliente, endereco, cidade, CEP, codigo_produto, nome_produto, valor_produto, quantidade_comprada, valor_total_compra)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    row['nome cliente'],
                    row['endereco'],
                    row['cidade'],
                    row['CEP'],
                    row['codigo_produto'],
                    row['nome produto'],
                    row['valor_produto'],
                    row['quantidade_comprada'],
                    row['valor_total_compra']
                ))
        
        self.connection.commit()
        cursor.close()
        self.db.close()

def read_config(file_path):
    config = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line and "=" in line:
                name, value = line.split('=', 1)
                config[name.strip()] = value.strip()
    return config