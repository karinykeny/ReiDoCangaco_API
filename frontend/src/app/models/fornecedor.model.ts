export class Fornecedor {
    cod_fornecedor: number;

    constructor(
        public cnpj_cpf: string,
        public nome_fantasia: string,
        public razao_social: string,
        public ativo: string 
        ) {}
}