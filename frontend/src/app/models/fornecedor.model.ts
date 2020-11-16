import { Contato } from './contato.model';

export class Fornecedor {
    cod_fornecedor: number;
    cnpj_cpf: string;
    nome_fantasia: string;
    razao_social: string;
    ativo: string;
    contatos: Array<Contato>;
}