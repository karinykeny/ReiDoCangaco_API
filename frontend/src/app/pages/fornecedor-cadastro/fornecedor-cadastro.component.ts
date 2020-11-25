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
  cpf_cnpj : any;
  public paginaAtual = 1;
  estados: Array<string> = ["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"];

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
      cnpj_cpf: [fornecedor.cnpj_cpf, [Validators.required, Validators.minLength(11), Validators.maxLength(18)]],
      nome_fantasia: [fornecedor.nome_fantasia, [Validators.required, Validators.minLength(3), Validators.maxLength(150)]],
      razao_social: [fornecedor.razao_social, [Validators.required, Validators.minLength(3), Validators.maxLength(150)]],
      ativo: [fornecedor.ativo, [Validators.required, Validators.minLength(3), Validators.maxLength(3)]]
    })
  }

  createFormContato(contato: Contato) {
    this.formContato = this.formBuilder.group({
      nome: [contato.nome, [Validators.required, Validators.minLength(3), Validators.maxLength(150)]],
      logradouro: [contato.logradouro, [Validators.required, Validators.minLength(3), Validators.maxLength(150)]],
      numero: [contato.numero, [Validators.required, Validators.minLength(1), Validators.maxLength(10)]],
      bairro: [contato.bairro, [Validators.required, Validators.minLength(3), Validators.maxLength(50)]],
      cidade: [contato.cidade, [Validators.required, Validators.minLength(3), Validators.maxLength(50)]],
      estado: [contato.estado, [Validators.required, Validators.minLength(2), Validators.maxLength(2)]],
      cep: [contato.cep, [Validators.required, Validators.minLength(8), Validators.maxLength(8)]],
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
      this.alertService.success(`Fornecedor ${newFornecedor.nome_fantasia} criada com sucesso`);
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
      this.alertService.success(`Contato ${newContato.nome} criada com sucesso`);
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

  isCPF(): boolean{
    return this.formFornecedor.value.cnpj_cpf == null ? true : this.formFornecedor.value.cnpj_cpf.length < 12 ? true : false;
 }

  getCpfCnpjMask(): string{
    return this.isCPF() ? '000.000.000-009' : '00.000.000/0000-00';
 }

 resetForm(): void {
  this.formContato.reset();
}
}
