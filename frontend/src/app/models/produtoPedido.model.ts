export class ProdutoPedido {
    cod_nota: number;

    constructor(
        public qtd_produto: number,
        public valor_parcial: number,
        public cod_pedido: number,
        public id_produto: number
    ) {}
}