import { AlertService } from 'src/app/services/alert.service';
import { ContatoService } from './../../services/contato.service';
import { FornecedorService } from './../../services/fornecedor.service';
import { Contato } from './../../models/contato.model';
import { Fornecedor } from './../../models/fornecedor.model';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Component, OnInit } from '@angular/core';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-fornecedor-cadastro',
  templateUrl: './fornecedor-cadastro.component.html',
  styleUrls: ['./fornecedor-cadastro.component.css']
})
export class FornecedorCadastroComponent implements OnInit {
  formFornecedor: FormGroup;
  formContato: FormGroup;
  fornecedor: Fornecedor;
  contatos = new Array<Contato>();
  contatoEdit: Contato = new Contato();
  loading = false;
  submitted = false;
  cpf: boolean = true;
  public paginaAtual = 1;


  constructor(
    private formBuilder: FormBuilder,
    private fornecedorService: FornecedorService,
    private contatoService: ContatoService,
    private alertService: AlertService,
    ) { }

  ngOnInit(): void {
    this.createFormFornacedor(new Fornecedor);
    this.createFormContato(new Contato);
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
    this.submitted = true;
    this.alertService.clear();
    if (this.formFornecedor.invalid) { 
      return; 
    }
    this.loading = true;

    const newFornecedor = new Fornecedor();
    newFornecedor.cnpj_cpf = this.formFornecedor.value.cnpj_cpf
    newFornecedor.nome_fantasia = this.formFornecedor.value.nome_fantasia
    newFornecedor.razao_social = this.formFornecedor.value.razao_social
    newFornecedor.ativo = this.formFornecedor.value.ativo

    this.fornecedorService.createFornecedor(newFornecedor)
    .pipe(first()).subscribe(result => {
      this.alertService.success("Fornecedor criada com sucesso");
      this.fornecedor = result;
      document.getElementById('closeAddModal').click();
    }, error => {
      this.alertService.error(error.error.mensagem);
      document.getElementById('closeAddModal').click();
      this.loading = false;
    })
  }

  getInfModal(contato: Contato) {
    this.contatoEdit = contato;
  }

  onSubmitContato() {
    this.submitted = true;
    this.alertService.clear();
    if (this.formContato.invalid) { 
      return; 
    }

    this.loading = true;
    const newContato = this.createContato();

    this.contatoService.createContato(newContato)
    .pipe(first()).subscribe(result => {
      this.alertService.success("Contato criada com sucesso");
      this.contatoEdit = result;
      this.contatos.push(this.contatoEdit);
      document.getElementById('closeAddModal').click();
    }, error => {
      this.alertService.error(error.error.mensagem);
      document.getElementById('closeAddModal').click();
      this.loading = false;
    })
  }

  createContato(): Contato {
    let contato = new Contato();
    contato.nome = this.formContato.value.nome;
    contato.logradouro = this.formContato.value.logradouro;
    contato.numero = this.formContato.value.numero;
    contato.bairro = this.formContato.value.bairro;
    contato.cidade = this.formContato.value.cidade;;
    contato.estado = this.formContato.value.estado;
    contato.cep = this.formContato.value.cep;
    contato.complemento = this.formContato.value.complemento;
    contato.telefone_fixo = this.formContato.value.telefone_fixo;
    contato.celular = this.formContato.value.celular;
    contato.email = this.formContato.value.email;
    contato.cod_fornecedor = this.fornecedor.cod_fornecedor;
    return contato;
  }

  clean() {
    this.submitted = false;
    this.loading = false;
  }
}
