export class Vendedor {
    codVendedor: number;
    ativo: boolean;

    constructor(
      public nomeVendedor: string,
      public login: string,
      public senha: string
    ) { }
  }