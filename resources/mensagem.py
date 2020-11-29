# Produto
def produtoEmUso(id_produto):
    return {'message': 'Produto com id "{}" está em uso.'
            .format(id_produto)}, 400


def produtoJaExiste(cod_produto):
    return {'message': 'Produto com código "{}" já existe.'
            .format(cod_produto)}, 400


produtoNaoEncontrado = {'message': 'Produto não encontrado.'}, 404

erroSalvarProduto = {'message': 'Erro ao salvar o produto.'}, 500

erroExcluirProduto = {'message': 'Erro ao excluir o produto.'}, 500

produtoExcluido = {'message': 'Produto excluído.'}


# Categoria
def categoriaEmUso(cod_categoria):
    return {'message': 'Categoria com código "{}" está em uso.'
            .format(cod_categoria)}, 400


def categoriaJaExiste(nome_categoria):
    return {'message': 'Categoria "{}" já existe.'
            .format(nome_categoria)}, 400


categoriaNaoEncontrada = {'message': 'Categoria não encontrado.'}, 404

erroSalvarCategoria = {'message': 'Erro ao salvar a categora.'}, 500

erroExcluirCategoria = {'message': 'Erro ao excluir a categoria.'}, 500

categoriaExcluida = {'message': 'Categoria excluída.'}


# Fornecedor
def fornecedorEmUso(cod_fornecedor):
    return {'message': 'Fornecedor com código "{}" está em uso.'
            .format(cod_fornecedor)}, 400


def fornecedorJaExiste(cod_fornecedor):
    return {'message': 'Fornecedor com código "{}" já existe.'
            .format(cod_fornecedor)}, 400


def cnpjCpfJaExiste(cnpj_cpf):
    return {'message': 'CNPJ/CPF "{}" já foi cadastrado.'
            .format(cnpj_cpf)}, 400


erroSalvarFornecedor = {'message': 'Erro ao salvar o fornecedor.'}, 500

fornecedorNaoEncontrado = {'message': 'Fornecedor não encontrado.'}, 404

erroExcluirFornecedor = {'message': 'Erro ao excluir o fornecedor.'}, 500

fornecedorExcluido = {'message': 'Fornecedor excluído.'}


# Vendedor
def vendedorEmUso(cod_vendedor):
    return {'message': 'Vendedor com código "{}" está em uso.'
            .format(cod_vendedor)}, 400


def loginExiste(login):
    return {'message': 'Login "{}" já existe.'.format(login)}, 400


erroSalvarVendedor = {'message': 'Erro ao salvar o fornecedor.'}, 500

vendedorNaoEncontrado = {'message': 'Vendedor não encontrado.'}, 404

erroExcluirVendedor = {'message': 'Erro ao excluir o vendedor.'}, 500

vendedorExcluido = {'message': 'Vendedor excluído.'}

vendedorCriado = {'message': 'Vendedor criado com sucesso!'}, 201

loginInvalido = {'message': 'login ou senha inválidos!'}, 401

logout = {'message': 'Logout com sucesso!'}, 200


# Forma de pagamento
def formaPagamentoEmUso(cod_formaPgameno):
    return {'message': 'Forma de pagamento com código "{}" está em uso.'
            .format(cod_formaPgameno)}, 400


def fPJaExiste(tipo_formaPagamento):
    return {'message': 'Forma de pagamento "{}" já existe.'
            .format(tipo_formaPagamento)}, 400


FPNaoEncontrada = {'message': 'Forma de pagamento não encontrado.'}, 404

erroSalvarFP = {'message': 'Erro ao salvar a forma de pagamento.'}, 500

erroExcluirFP = {'message': 'Erro ao excluir a forma de pagamento.'}, 500

FPExcluida = {'message': 'Forma de pagamento excluída.'}


# Pedido
def pedidoEmUso(cod_pedido):
    return {'message': 'Pedido com código "{}" está em uso.'
            .format(cod_pedido)}, 400


pedidoNaoEncontrado = {'message': 'Pedido não encontrado.'}, 404

erroSalvarPedido = {'message': 'Erro ao salvar o pedido.'}, 500

erroExcluirPedido = {'message': 'Erro ao excluir o pedido.'}, 500

pedidoExcluido = {'message': 'Pedido excluído.'}


# Contato
def contatoJaExiste(cod_contato):
    return {'message': 'Contato com código "{}" já existe.'
            .format(cod_contato)}, 400


contatoNaoEncontrado = {'message': 'Contato não encontrado.'}, 404

erroSalvarContato = {'message': 'Erro ao salvar o contato.'}, 500

erroExcluirContato = {'message': 'Erro ao excluir o contato.'}, 500

contatoExcluido = {'message': 'Contato excluído.'}


# Produto/Pedido
pPNaoEncontrado = {'message': 'Produto/Pedido não encontrado.'}, 404

erroSalavarPP = {'message': 'Erro ao salvar o Produto/Pedido.'}, 500

erroExcluirPP = {'message': 'Erro ao excluir o Produto/Pedido.'}, 500

pPExcluido = {'message': 'Produto/Pedido excluído.'}
