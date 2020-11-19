import { FornecedorService } from './../../services/fornecedor.service';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Fornecedor } from 'src/app/models/fornecedor.model';
import { AlertService } from 'src/app/services/alert.service';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-fornecedor-list',
  templateUrl: './fornecedor-list.component.html',
  styleUrls: ['./fornecedor-list.component.css']
})
export class FornecedorListComponent implements OnInit {

  fornecedores = new Array<Fornecedor>();
  fornecedorEdit: Fornecedor = new Fornecedor();
  formFornecedor: FormGroup;
  loading = false;
  submitted = false;
  public paginaAtual = 1;

  constructor(
    private fornecedorService: FornecedorService,
    private alertService: AlertService,
    private formBuilder: FormBuilder,
    ) { }

  ngOnInit(): void {
    this.createForm(new Fornecedor());
    this.getFornecedores();
  }

  createForm(fornecedor: Fornecedor) {
    this.formFornecedor = this.formBuilder.group({
      cnpj_cpf: [fornecedor.cnpj_cpf, Validators.nullValidator],
      nome_fantasia: [fornecedor.nome_fantasia, Validators.nullValidator],
      razao_social: [fornecedor.razao_social, Validators.nullValidator],
      ativo: [fornecedor.ativo, Validators.nullValidator],
    })
  }

  getFornecedores(): void {
    this.fornecedorService.getAll().subscribe(
      result => {
        this.fornecedores = result.fornecedores;
    });
  }

  getEditModal(fornecedor: Fornecedor): void {
    this.fornecedorEdit = fornecedor;
  }

  getAddModal(): void {
    this.fornecedorEdit = null;
  }

  getDeleteModal(fornecedor: Fornecedor): void {
    this.fornecedorEdit = fornecedor;
  }

  get ffp() { return this.formFornecedor.controls; }


  editFornecedor(): void {
    this.submitted = true;
    this.alertService.clear();
    if (this.formFornecedor.invalid) { 
      return; 
    }
    this.loading = true; 

    const infFornecedor = new Fornecedor();
    infFornecedor.cod_fornecedor = this.formFornecedor.value.cod_fornecedor
    infFornecedor.cnpj_cpf = this.formFornecedor.value.cnpj_cpf
    infFornecedor.nome_fantasia = this.formFornecedor.value.nome_fantasia
    infFornecedor.razao_social = this.formFornecedor.value.razao_social
    infFornecedor.ativo = this.formFornecedor.value.ativo

    this.fornecedorService.putFornecedor(infFornecedor)
    .pipe(first()).subscribe( reult => {
      this.alertService.success(`Fornecedor com código ${infFornecedor.cod_fornecedor} foi alterada`);
      this.getFornecedores();
      document.getElementById('closeModal').click();
    }, error => {
      this.alertService.error(error.mensagem);
      document.getElementById('closeModal').click();
      this.loading = false;
    })
  }

  deleteFornecedor(): void {
    this.alertService.clear();
    this.loading = true;

    this.fornecedorService.deleteFornecedor(this.fornecedorEdit.cod_fornecedor)
    .pipe(first()).subscribe( result => {
      this.alertService.success("Fornecedor excluído com sucesso");
      this.getFornecedores();
      document.getElementById('closeDelete').click();

    }, error => {
      this.alertService.error(error.error.mensagem)
      document.getElementById('closeDelete').click();
      this.loading = false;
    })
  }

  clean(): void {
    this.submitted = false;
    this.loading = false;
  }

}
