export class FormaPagamento {
    cod_formaPgameno: number;

    constructor(
        public tipo_formaPagamento: string,
        public descricao_formaPagamento: string
    ) {}
}