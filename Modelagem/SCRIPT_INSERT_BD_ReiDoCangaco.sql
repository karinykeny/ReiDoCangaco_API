INSERT INTO categoria
		(nome_categoria)
VALUES	('Laticinios'),
		('Carnes'),
        ('Alimentos'),
        ('Peixes'),
        ('Aves'),
        ('Limpeza'),
        ('Higiene'),
        ('Bebidas');
        
/* SELECT * FROM categoria; */ 

INSERT INTO produto
	(cod_produto, cod_categoria, nome_produto, valor_produto, ativo)
VALUES
	('CodLEIT1', '1', 'Leite 1L', 5.50, 'SIM'),
	('CodIOR', '1', 'Iogurte 1L', 4.00, 'SIM'),
	('CodSOR', '1', 'Sorvete 1KG', 10.00, 'SIM'),
	('CodACHO', '1', 'Achocolatado 1L', 6.50, 'NAO'),
	('CodLEIT2', '1', 'Leite em Po 250g', 3.40, 'NAO'),
    
	('Cod10E', '2', 'Picanha (peça)', 90.00, 'SIM'),
	('Cod11E', '2', 'Costela Suina', 40.00, 'SIM'),
	('Cod12E', '2', 'Linguica Toscana', 10.00, 'SIM'),	
	('Cod13E', '2', 'Alcatra (peça)', 55.00, 'NAO'),
	('Cod14E', '2', 'Carne Moida', 25.00, 'NAO'),

	('CodCAF1', '3', 'Cafe Moido 500g', 5.50, 'SIM'),
	('CodCAF2', '3', 'Cafe em Graos 1KG', 35.00, 'NAO'),
	('CodARZ', '3', 'Arroz Parborizado 1KG', 10.00, 'SIM'),
	('CodFEI', '3', 'Feijao Preto 1KG', 8.00, 'SIM'),

	('CodPXE1', '4', 'Tilapia 1KG', 20.00,	'SIM'),
	('CodPXE9', '4', 'Bacalhau 1KG', 40.00, 'NAO'),
    
    ('CodAVE1', '5', 'Galinha 1KG', 10.00, 'SIM'),    
	('CodAVE0', '5', 'Codorna 1KG', 15.00, 'NAO'),    
    
	('CodLIMP1', '6', 'Detergente Liquido',	 2.95, 'SIM'),
	('CodLIMP2', '6', 'Amaciante', 8.00, 'SIM'),
	('CodLIMP5', '6', 'Inseticida', 10.00, 'NAO'),
    
	('CodHIG2', '7', 'Shampoo da Xuxa', 10.00, 'SIM'),	
	('CodHIG9', '7', 'Sabonete', 5.00, 'SIM'),
	
    ('CodBEB1', '8', 'Polpa de Fruta',	15.00, 'SIM'),
    ('CodBEB5', '8', 'Cerveja Skol Lata', 5.00, 'SIM'),
	('CodBEB6', '8', 'Cha Mate', 3.00, 'SIM');

/* SELECT * FROM produto; */	
	
INSERT INTO	formaPagamento
	(tipo_formaPagamento, descricao_formaPagamento)
VALUES
	('Dinheiro','A Vista'),
	('Cartao|Debito', 'A Vista'),
	('Cartao|Credito', 'A Vista'),
	('Cartao|Credito', 'Parcelado - 2x'),
	('Cartao|Credito', 'Parcelado - 3x'),
	('Cartao|Credito', 'Parcelado - 4x'),
	('Cartao|Credito', 'Parcelado - 5x'),
	('Cartao|Credito', 'Parcelado - 6x'),
	('Cartao|Credito', 'Parcelado - 7x'),
	('Cartao|Credito', 'Parcelado - 8x'),
	('Cartao|Credito', 'Parcelado - 9x'),
	('Cartao|Credito', 'Parcelado - 10x'),
	('Cartao|Credito', 'Parcelado - 11x'),
	('Cartao|Credito', 'Parcelado - 12x');

/* SELECT * FROM formaPagamento; */	

INSERT INTO vendedor
	(nome_vendedor, login, senha, ativo)
VALUES
    ('Administrador', 'administrador', 'adm123', 'SIM'),
	('João Gilberto', 'joao.gilberto', '231181', 'SIM'),
	('Kariny', 'kariny.dev', 'eunaosei',	'SIM'),
	('Vendedor Teste',	'vendedor.teste', '123456',	'NAO');  
	
/* SELECT * FROM vendedor; */	

INSERT INTO fornecedor
	(nome_fantasia, cnpj_cpf, ativo)
VALUES
    ('Seu Ze', '36479162005', 'SIM'),
	('Peixes LDTA', '21304873000168', 'SIM'),
	('Mercadinho Caruaru', '07499072000174', 'SIM'),
	('Dona Joana',	'00044311036', 'NAO'); 

/* SELECT * FROM fornecedor; */	

INSERT INTO	contato
	(cod_fornecedor, logradouro, numero, bairro, cidade, estado, cep, complemento, telefone_fixo, celular, email)
VALUES
	(1, 'Rua Poeta Ze Vicente da Paraiba',	104, 'Rendeiras', 'Caruaru', 'PE', 55022798, '', '8134150256', '81998890001', 'seuze@hotmail.com'),
    (2, 'Travessa Severino de Oliveira Melo',	90, 'Sao Francisco', 'Caruaru', 'PE', 55006065, '', '8134350554', '81997793501', 'peixaria@gmail.com'),
    (3, 'Rua Severino Leite da Silva',	100, 'Alto do Moura', 'Caruaru', 'PE', 55040255, '', '8133200250', '81986669550', 'mercadinho@hotmail.com'),
    (4, 'Rua Sebastiao Cabral',	50, 'Cidade Alta', 'Caruaru', 'PE', 55031060, '', '8133150256', '81996890121', 'donajoana12@hotmail.com');
    
/* SELECT * FROM contato; */

INSERT INTO	pedido
	(cod_vendedor, cod_formaPagamento, data_pedido, valor_pedido, status)
VALUES
	(2, 1, (SELECT CURDATE()),	90.00, 'FATURADO'),
	(2, 3, (SELECT CURDATE()),	23.00, 'FATURADO'),
   
    (3, 2, (SELECT CURDATE()),	56.00, 'FATURADO'),
	(3, 4, (SELECT CURDATE()),	95.00, 'FATURADO'),
    
   	(4, 1, (SELECT CURDATE()),	20.00, 'CANCELADO'),
	(4, 5, (SELECT CURDATE()),	40.00, 'CANCELADO');
    
/* SELECT * FROM pedido; */	

INSERT INTO produto_pedido
	(cod_pedido, id_produto, cod_produto, qtd_produto, valor_parcial)
VALUES

/* pedidos João Gilberto*/	

	(1, 6,'Cod10E' , 1, 90.00),
    
    (2, 1,'CodLEIT1' , 2, 11.00),
	(2,	4,'CodACHO' , 1, 6.50),
    (2, 11,'CodCAF1' , 1, 5.50),
	
/* pedidos Kariny*/	

	(3, 15,'CodPXE1' , 2, 40.00),
    (3, 20,'CodLIMP2' , 2, 16.00),
	
    (4,	24,'CodBEB1' , 3, 45.00),
    (4, 25,'CodBEB5' , 10, 50.00),
    
/* pedidos Vendedor Teste*/	

    (5,	2,'CodIOR' , 5, 20.00),
    
    (6, 7,'Cod11E' , 1, 40.00);  

/* SELECT * FROM produto_pedido; */	