export class Produto {
    id_produto: number;

    constructor(
        public cod_produto: string,
        public nome_produto: string,
        public valor_produto: number,
        public ativo: string,
        public cod_categoria: number,
        public cod_fornecedor: number
    ) {}
}