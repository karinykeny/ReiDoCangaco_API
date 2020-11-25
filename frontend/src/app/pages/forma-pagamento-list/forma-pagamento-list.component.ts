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

  formasPagamento = new Array<FormaPagamento>();
  formasPagamento_db = new Array<FormaPagamento>();
  fpEdit: FormaPagamento = new FormaPagamento();
  formFP: FormGroup;
  loading = false;
  submitted = false;
  isAddMode: boolean;
  id: number;
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

  getIsAddMode(): void {
    if (this.fpEdit.cod_formaPgameno) {
      this.id = this.fpEdit.cod_formaPgameno;
      this.formaPagamentoService.getById(this.id)
        .pipe(first()).subscribe(x => {
          this.formFP.patchValue(x);
          this.isAddMode = false;
        });
    }
  }

  getAddMode(): void {
    this.isAddMode = true;
    this.formFP.reset();
  }

  createForm(fp: FormaPagamento) {
    this.formFP = this.formBuilder.group({
      tipo_formaPagamento: [fp.tipo_formaPagamento, [Validators.required, Validators.minLength(3), Validators.maxLength(50)] ],
      descricao_formaPagamento: [fp.descricao_formaPagamento, [Validators.required, Validators.minLength(3), Validators.maxLength(50)] ]
    })
  }

  onSubmit() {
    this.submitted = true;
    this.alertService.clear();
    if (this.formFP.invalid) {
        return;
    }

    this.loading = true;
    if (this.isAddMode) {
        this.saveFormasPagamento();
    } else {
        this.editFormasPagamento();
    }
  }

  getFormasPagamento(): void {
    this.formaPagamentoService.getAll().subscribe(
      result => {
        this.formasPagamento_db = result.formasPagamento;
        this.formasPagamento = result.formasPagamento;
    });
  }

  getInfModal(fp: FormaPagamento): void {
    this.fpEdit = fp;
  }

  get fp() { return this.formFP.controls; }

  saveFormasPagamento(): void {
    const newFP = new FormaPagamento();
    newFP.tipo_formaPagamento = this.formFP.value.tipo_formaPagamento
    newFP.descricao_formaPagamento = this.formFP.value.descricao_formaPagamento

    this.formaPagamentoService.createFormaPagamento(newFP)
    .subscribe(() => {
      this.alertService.success(`Forma de pagamento ${newFP.tipo_formaPagamento} criada com sucesso`);
      this.getFormasPagamento();
      document.getElementById('closeAddModal').click();
    },error => {
      this.alertService.error(error);
      document.getElementById('closeAddModal').click();
      this.loading = false;
    })
  }


  editFormasPagamento(): void {
    const infFP = new FormaPagamento();
    infFP.cod_formaPgameno = this.id;
    infFP.tipo_formaPagamento = this.formFP.value.tipo_formaPagamento
    infFP.descricao_formaPagamento = this.formFP.value.descricao_formaPagamento

    this.formaPagamentoService.putFormaPagamento(infFP)
    .pipe(first()).subscribe(() => {
      this.alertService.success(`Forma de pagamento com código ${infFP.cod_formaPgameno} foi alterada`);
      this.getFormasPagamento();
      document.getElementById('closeAddModal').click();
    }, error => {
      this.alertService.error(error);
      document.getElementById('closeAddModal').click();
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
      this.alertService.error(error)
      document.getElementById('closeDelete').click();
      this.loading = false;
    })
  }

  clean(): void {
    this.submitted = false;
    this.loading = false;
  }

  filtrar(value: any) {
    if(!value) {
      this.formasPagamento = this.formasPagamento_db;
   } else {
     this.formasPagamento = this.formasPagamento_db.filter( fp => 
      fp.tipo_formaPagamento.trim().toLowerCase().includes(value.trim().toLowerCase())
     );
   }
  }

  getForm(): void {
    this.formFP.value.tipo_formaPagamento = this.fpEdit.tipo_formaPagamento;
    this.formFP.value.descricao_formaPagamento = this.fpEdit.descricao_formaPagamento;
  }
}
