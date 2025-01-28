import schedule
import time
from data_importacao import DataImporter, read_config

def job():
    config = read_config('config.txt')
    importer = DataImporter(config)
    importer.import_data_from_csv('data/vendas_produtos.csv')
    print("Dados importados com sucesso!")

def main():

    # Executa a primeira carga
    job()

    # Agendando a execução a cada 6 horas
    schedule.every(6).hours.do(job)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
