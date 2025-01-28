import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.connection = None
    
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print("Conexão bem-sucedida ao banco de dados MySQL")
        except Error as e:
            print(f"Erro ao conectar ao banco de dados MySQL: {e}")
        return self.connection
    

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Conexão com o banco de dados MySQL foi fechada")
