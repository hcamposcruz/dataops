create table dados.importacao (
	id INT NOT NULL AUTO_INCREMENT,
	nome_cliente 	varchar(100) DEFAULT NULL,
	endereco 		varchar(200) DEFAULT NULL,
	cidade 			varchar(100) DEFAULT NULL,
	CEP 			varchar(20) DEFAULT NULL,
	codigo_produto 	int DEFAULT NULL,
	nome_produto 	varchar(100) DEFAULT NULL,
	valor_produto 	int DEFAULT NULL,
	quantidade_comprada int DEFAULT NULL,
	valor_total_compra 	int DEFAULT NULL,
	PRIMARY KEY (`id`)
)