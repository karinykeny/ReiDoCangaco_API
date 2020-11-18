import { Contato } from './../../models/contato.model';
import { Fornecedor } from './../../models/fornecedor.model';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-fornecedor-cadastro',
  templateUrl: './fornecedor-cadastro.component.html',
  styleUrls: ['./fornecedor-cadastro.component.css']
})
export class FornecedorCadastroComponent implements OnInit {
  formFornecedor: FormGroup;
  formContato: FormGroup;
  contatos: Contato[];
  contatoEdit: Contato;
  loading = false;
  submitted = false;
  cpf: boolean = true;
  public paginaAtual = 1;

  constructor(private formBuilder: FormBuilder) { }

  ngOnInit(): void {
  }

  createFormFornacedor(fornecedor: Fornecedor) {
    this.formFornecedor = this.formBuilder.group({
      cnpj_cpf: [fornecedor.cnpj_cpf, Validators.nullValidator],
      nome_fantasia: [fornecedor.nome_fantasia, Validators.nullValidator],
      razao_social: [fornecedor.razao_social, Validators.nullValidator],
      ativo: [fornecedor.ativo, Validators.nullValidator]
    })
  }

  createFormContato(contato: Contato) {
    this.formContato = this.formBuilder.group({
      nome: [contato.nome, Validators.nullValidator],
      logradouro: [contato.logradouro, Validators.nullValidator],
      numero: [contato.numero, Validators.nullValidator],
      bairro: [contato.bairro, Validators.nullValidator],
      cidade: [contato.cidade, Validators.nullValidator],
      estado: [contato.estado, Validators.nullValidator],
      cep: [contato.cep, Validators.nullValidator],
      complemento: [contato.complemento],
      telefone_fixo: [contato.telefone_fixo],
      celular: [contato.celular],
      email: [contato.email, Validators.email]
    })
  }

  get f() { return this.formFornecedor.controls; }

  get c() { return this.formContato.controls; }

  onSubmitFornecedor() {

  }

  getInfModal(contato: Contato) {

  }

  saveContato() {

  }

  editContato() {
    
  }
  

  onSubmitContato() {

  }

  clean() {

  }
}
