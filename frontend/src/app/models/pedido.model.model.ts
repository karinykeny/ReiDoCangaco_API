export class Pedido {
    cod_pedido: number;

    constructor(
        public valor_pedido: number,
        public data_pedido: string,
        public status: string,
        public cod_vendedor: number,
        public cod_formaPgameno: number
    ) {}
}