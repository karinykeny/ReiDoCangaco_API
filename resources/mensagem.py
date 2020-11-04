# Produto
def produtoEmUso(id_produto):
    return {'mensagem': 'Produto com id "{}" está em uso.'
            .format(id_produto)}, 400


# Categoria
def categoriaEmUso(cod_categoria):
    return {'mensagem': 'Categoria com código "{}" está em uso.'
            .format(cod_categoria)}, 400


def categoriaJaExiste(nome_categoria):
    return {'mensagem': 'Categoria "{}" já existe.'
            .format(nome_categoria)}, 400


categoriaNaoEncontrada = {'mensagem': 'Categoria não encontrado.'}, 404

erroSalvarCategoria = {'mensagem': 'Erro ao salvar a categora.'}, 500

erroExcluirCategoria = {'mensagem': 'Erro ao excluir a categoria.'}, 500

categoriaExcluida = {'mensagem': 'Categoria excluída.'}, 204


# Fornecedor
def fornecedorEmUso(cod_fornecedor):
    return {'mensagem': 'Fornecedor com código "{}" está em uso.'
            .format(cod_fornecedor)}, 400


def fornecedorJaExiste(cod_fornecedor):
    return {'mensagem': 'Fornecedor com código "{}" já existe.'
            .format(cod_fornecedor)}, 400


def cnpjCpfJaExiste(cnpj_cpf):
    return {'mensagem': 'CNPJ/CPF "{}" já existe.'
            .format(cnpj_cpf)}, 400


erroSalvarFornecedor = {'mensagem': 'Erro ao salvar o fornecedor.'}, 500

fornecedorNaoEncontrado = {'mensagem': 'Fornecedor não encontrado.'}, 404

erroExcluirFornecedor = {'mensagem': 'Erro ao excluir o fornecedor.'}, 500

fornecedorExcluido = {'mensagem': 'Fornecedor excluído.'}, 204
