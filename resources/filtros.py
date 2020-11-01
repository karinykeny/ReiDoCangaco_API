def normalize_path_params_produto(nome_produto=None,
                                  valor_max=10000,
                                  valor_min=0,
                                  ativo="sim"):

    if nome_produto:
        return {
            'nome_produto': nome_produto,
            'valor_max': valor_max,
            'valor_min': valor_min,
            'ativo': ativo
        }

    return {
        'valor_max': valor_max,
        'valor_min': valor_min,
        'ativo': ativo
    }


consulta_sem_nome_produto = "SELECT * FROM produto \
                WHERE valor_produto < ? AND valor_produto > ? \
                AND ativo = ?"

consulta_com_nome_produto = "SELECT * FROM produto \
                WHERE nome_produto LIKE ? AND \
                valor_produto < ? AND valor_produto > ? \
                AND ativo = ?"


def normalize_path_params_fornecedor(cnpj_cpf=None,
                                     nome_fantasia=None,
                                     ativo="sim"):
    params = {}
    if cnpj_cpf:
        params['cnpj_cpf'] = cnpj_cpf
    if nome_fantasia:
        params['nome_fantasia'] = nome_fantasia

    params['ativo'] = ativo
    return params


consulta_fornecedor = "SELECT * FROM fornecedor WHERE ativo = ?"
