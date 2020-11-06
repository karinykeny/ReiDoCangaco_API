# Produto
def produtoEmUso(id_produto):
    return {'mensagem': 'Produto com id "{}" está em uso.'
            .format(id_produto)}, 400


def produtoJaExiste(cod_produto):
    return {'mensagem': 'Produto com código "{}" já existe.'
            .format(cod_produto)}, 400


produtoNaoEncontrado = {'mensagem': 'Produto não encontrado.'}, 404

erroSalvarProduto = {'mensagem': 'Erro ao salvar o produto.'}, 500

erroExcluirProduto = {'mensagem': 'Erro ao excluir o produto.'}, 500

produtoExcluido = {'mensagem': 'Produto excluído.'}, 204


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


# Vendedor
def vendedorEmUso(cod_vendedor):
    return {'mensagem': 'Vendedor com código "{}" está em uso.'
            .format(cod_vendedor)}, 400


def loginExiste(login):
    return {'mensagem': 'Login "{}" já existe.'.format(login)}, 400


vendedorNaoEncontrado = {'mensagem': 'Vendedor não encontrado.'}, 404

erroExcluirVendedor = {'mensagem': 'Erro ao excluir o vendedor.'}, 500

fornecedorExcluido = {'mensagem': 'Vendedor excluído.'}, 204

vendedorCriado = {'mensagem': 'Vendedor criado com sucesso!'}, 201

loginInvalido = {'mensagem': 'login ou senha inválidos!'}, 401

logout = {'mensagem': 'Logout com sucesso!'}, 200


# Forma de pagamento
def formaPagamentoEmUso(cod_formaPgameno):
    return {'mensagem': 'Forma de pagamento com código "{}" está em uso.'
            .format(cod_formaPgameno)}, 400


def fPJaExiste(tipo_formaPagamento):
    return {'mensagem': 'Forma de pagamento "{}" já existe.'
            .format(tipo_formaPagamento)}, 400


FPNaoEncontrada = {'mensagem': 'Forma de pagamento não encontrado.'}, 404

erroSalvarFP = {'mensagem': 'Erro ao salvar a forma de pagamento.'}, 500

erroExcluirFP = {'mensagem': 'Erro ao excluir a forma de pagamento.'}, 500

FPExcluida = {'mensagem': 'Forma de pagamento excluída.'}, 204


# Pedido
def pedidoEmUso(cod_pedido):
    return {'mensagem': 'Pedido com código "{}" está em uso.'
            .format(cod_pedido)}, 400


pedidoNaoEncontrado = {'mensagem': 'Pedido não encontrado.'}, 404

erroSalvarPedido = {'mensagem': 'Erro ao salvar o pedido.'}, 500

erroExcluirPedido = {'mensagem': 'Erro ao excluir o pedido.'}, 500

pedidoExcluido = {'mensagem': 'Pedido excluído.'}, 204


# Contato
def contatoJaExiste(cod_contato):
    return {'mensagem': 'Contato com código "{}" já existe.'
            .format(cod_contato)}, 400


contatoNaoEncontrado = {'mensagem': 'Contato não encontrado.'}, 404

erroSalvarContato = {'mensagem': 'Erro ao salvar o contato.'}, 500

erroExcluirContato = {'mensagem': 'Erro ao excluir o contato.'}, 500

contatoExcluido = {'mensagem': 'Contato excluído.'}, 204


# Produto/Pedido
pPNaoEncontrado = {'mensagem': 'Produto/Pedido não encontrado.'}, 404

erroSalavarPP = {'mensagem': 'Erro ao salvar o Produto/Pedido.'}, 500

erroExcluirPP = {'mensagem': 'Erro ao excluir o Produto/Pedido.'}, 500

pPExcluido = {'mensagem': 'Produto/Pedido excluído.'}, 204
