DROP DATABASE IF EXISTS REICANGACO;

CREATE DATABASE IF NOT EXISTS REICANGACO;

USE REICANGACO;

CREATE TABLE vendedor (
cod_vendedor		INTEGER			NOT NULL	AUTO_INCREMENT	PRIMARY KEY,
nome_vendedor		VARCHAR(150)	NOT NULL,
login				VARCHAR(50)		NOT NULL	UNIQUE,
senha				VARCHAR(50)		NOT NULL,
ativo				CHAR(3)			NOT NULL
CONSTRAINT ck_vendedor_ativo		CHECK(ativo IN ('SIM','NAO')) -- Permite apenas estes dois tipos de status.
);

CREATE TABLE fornecedor (
cod_fornecedor		INTEGER			NOT NULL	AUTO_INCREMENT	PRIMARY KEY,
nome_fantasia		VARCHAR(150)	NOT NULL,
cnpj_cpf			VARCHAR(50)		NOT NULL	UNIQUE,
ativo				CHAR(3)			NOT NULL
CONSTRAINT ck_fornecedor_ativo		CHECK(ativo IN ('SIM','NAO')) -- Permite apenas estes dois tipos de status.
);

CREATE TABLE contato (
cod_contato		INTEGER			NOT NULL	AUTO_INCREMENT		PRIMARY KEY,
cod_fornecedor	INTEGER			NOT NULL,
logradouro		VARCHAR(150)	NOT NULL,
numero			VARCHAR(10),
bairro			VARCHAR(50)		NOT NULL,
cidade			VARCHAR(50)		NOT NULL,
estado			CHAR(2)			NOT NULL,
cep				VARCHAR(8)		NOT NULL,
complemento		VARCHAR(150),
telefone_fixo	VARCHAR(10),
celular			VARCHAR(11),
email			VARCHAR(150),
FOREIGN KEY(cod_fornecedor) REFERENCES fornecedor(cod_fornecedor)
);

CREATE TABLE formaPagamento (
cod_formaPagamento			INTEGER		NOT NULL	AUTO_INCREMENT	PRIMARY KEY,
tipo_formaPagamento			VARCHAR(50)	NOT NULL,
descricao_formaPagamento	VARCHAR(50)	NOT NULL
);

CREATE TABLE categoria (
cod_categoria	INTEGER		NOT NULL	AUTO_INCREMENT	PRIMARY KEY,
nome_categoria	VARCHAR(50)	NOT NULL
);

CREATE TABLE produto (
id_produto		INTEGER			NOT NULL	AUTO_INCREMENT	PRIMARY KEY,
cod_produto		VARCHAR(50)		NOT NULL,
cod_categoria	INTEGER			NOT NULL,
nome_produto	VARCHAR(150)	NOT NULL,
valor_produto	FLOAT			NOT NULL,
ativo			CHAR(3)			NOT NULL,
FOREIGN KEY(cod_categoria)		REFERENCES categoria(cod_categoria),
CONSTRAINT ck_produto_ativo		CHECK(ativo IN ('SIM','NAO')) -- Permite apenas estes dois tipos de status.
);

CREATE TABLE pedido (
cod_pedido				INTEGER		NOT NULL	AUTO_INCREMENT	PRIMARY KEY,
cod_vendedor			INTEGER		NOT NULL,
cod_formaPagamento		INTEGER		NOT NULL,
data_pedido				VARCHAR(10)	NOT NULL,
valor_pedido			FLOAT		NOT NULL,
status					VARCHAR(50)	NOT NULL,
FOREIGN KEY(cod_vendedor)			REFERENCES vendedor(cod_vendedor),
FOREIGN KEY(cod_formaPagamento)		REFERENCES formaPagamento(cod_formaPagamento)
);

CREATE TABLE produto_pedido (
cod_pedido		INTEGER		NOT NULL,
id_produto		INTEGER		NOT NULL,
cod_produto		VARCHAR(50)	NOT NULL,
qtd_produto		INTEGER		NOT NULL,
valor_parcial 	FLOAT		NOT NULL,
FOREIGN KEY(cod_pedido)		REFERENCES pedido(cod_pedido),
FOREIGN KEY(id_produto) 	REFERENCES produto(id_produto)
);