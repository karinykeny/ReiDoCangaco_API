import { FormaPagamento } from './../../models/formaPagamento.model';
import { Component, OnInit } from '@angular/core';
import { first } from 'rxjs/operators';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AlertService } from 'src/app/services/alert.service';
import { FormaPagamentoService } from 'src/app/services/formaPagamento.service';

@Component({
  selector: 'app-forma-pagamento-list',
  templateUrl: './forma-pagamento-list.component.html',
  styleUrls: ['./forma-pagamento-list.component.css']
})
export class FormaPagamentoListComponent implements OnInit {

  formasPagamento: FormaPagamento[];
  fpEdit: FormaPagamento = new FormaPagamento();
  formFP: FormGroup;
  loading = false;
  submitted = false;
  public paginaAtual = 1;

  constructor(
    private formaPagamentoService: FormaPagamentoService,
    private alertService: AlertService,
    private formBuilder: FormBuilder,
    ) { }

  ngOnInit(): void {
    this.createForm(new FormaPagamento());
    this.getFormasPagamento();
  }

  createForm(fp: FormaPagamento) {
    this.formFP = this.formBuilder.group({
      tipo_formaPagamento: [fp.tipo_formaPagamento, Validators.nullValidator ],
      descricao_formaPagamento: [fp.descricao_formaPagamento, Validators.nullValidator ]
    })
  }

  getFormasPagamento(): void {
    this.formaPagamentoService.getAll().subscribe(
      result => {
        this.formasPagamento = result.formasPagamento;
    });
  }

  getEditModal(fp: FormaPagamento): void {
    this.fpEdit = fp;
  }

  getAddModal(): void {
    this.fpEdit = null;
  }

  getDeleteModal(fp: FormaPagamento): void {
    this.fpEdit = fp;
  }

  get ffp() { return this.formFP.controls; }

  saveFormasPagamento(): void {
    this.submitted = true;
    this.alertService.clear();
    if (this.formFP.invalid) { 
      return; 
    }
    this.loading = true;

    const newFP = new FormaPagamento();
    newFP.tipo_formaPagamento = this.formFP.value.tipo_formaPagamento
    newFP.descricao_formaPagamento = this.formFP.value.descricao_formaPagamento

    this.formaPagamentoService.createFormaPagamento(newFP)
    .pipe(first()).subscribe(result => {
      this.alertService.success("Forma de pagamento criada com sucesso");
      this.getFormasPagamento();
      document.getElementById('closeAddModal').click();
    }, error => {
      this.alertService.error(error.error.mensagem);
      document.getElementById('closeAddModal').click();
      this.loading = false;
    })
  }


  editFormasPagamento(): void {
    this.submitted = true;
    this.alertService.clear();
    if (this.formFP.invalid) { 
      return; 
    }
    this.loading = true; 

    const infFP = new FormaPagamento();
    infFP.cod_formaPgameno = this.fpEdit.cod_formaPgameno
    infFP.tipo_formaPagamento = this.formFP.value.tipo_formaPagamento
    infFP.descricao_formaPagamento = this.formFP.value.descricao_formaPagamento

    this.formaPagamentoService.putFormaPagamento(infFP)
    .pipe(first()).subscribe( reult => {
      this.alertService.success(`Forma de pagamento com código ${infFP.cod_formaPgameno} foi alterada`);
      this.getFormasPagamento();
      document.getElementById('closeModal').click();
    }, error => {
      this.alertService.error(error.mensagem);
      document.getElementById('closeModal').click();
      this.loading = false;
    })
  }

  deleteFormasPagamento(): void {
    this.alertService.clear();
    this.loading = true;

    this.formaPagamentoService.deleteFormaPagamento(this.fpEdit.cod_formaPgameno)
    .pipe(first()).subscribe( result => {
      this.alertService.success("Forma de pagamento excluída com sucesso");
      this.getFormasPagamento();
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
