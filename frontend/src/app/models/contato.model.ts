export class Contato {
    cod_contato: number;
    complemento: string;
    telefone_fixo: string;
    celular: string;
    email: string;

    constructor(
        public logradouro: string,
        public numero: string,
        public bairro: string,
        public cidade: string,
        public estado: string,
        public cep: string,
        public cod_fornecedor: number
    ) {}
}