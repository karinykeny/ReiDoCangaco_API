class ContatoModel:
    def __init__(self, cod_contato, logradouro, numero, bairro, cidade,
                 estado, cep, complemento, telefone_fixo, celular, email):
        self.cod_contato = cod_contato
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.complemento = complemento
        self.telefone_fixo = telefone_fixo
        self.celular = celular
        self.email = email
