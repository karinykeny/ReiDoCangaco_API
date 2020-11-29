import { Vendedor } from './../../models/vendedor.model';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Component, OnInit } from '@angular/core';
import { VendedorService } from 'src/app/services/vendedor.service';
import { AlertService } from 'src/app/services/alert.service';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-vendedor-cadastro',
  templateUrl: './vendedor-cadastro.component.html',
  styleUrls: ['./vendedor-cadastro.component.css']
})
export class VendedorCadastroComponent implements OnInit {
  formVendedor: FormGroup;
  vendedor: Vendedor;
  loading = false;
  submitted = false;
  statusList = ["Ativo","Inativo"];

  constructor(
    private formBuilder: FormBuilder,
    private vendedorService: VendedorService,
    private alertService: AlertService,
    ) { }

  ngOnInit(): void {
    this.createForm(new Vendedor);
  }

  createForm(vendedor: Vendedor) {
    this.formVendedor = this.formBuilder.group({
      nome_vendedor: [vendedor.nome_vendedor, [Validators.required, Validators.minLength(3), Validators.maxLength(150)]],
      login: [vendedor.login, [Validators.required, Validators.minLength(3), Validators.maxLength(50)]],
      senha: [vendedor.senha, [Validators.required, Validators.minLength(3), Validators.maxLength(50)]],
      ativo: [vendedor.ativo, Validators.required],
    })
  }

  get v() { return this.formVendedor.controls; }

  onSubmit() {
    this.submitted = true;
    this.alertService.clear();
    if (this.formVendedor.invalid) { 
      return; 
    }
    this.loading = true;

    const infVendedor = new Vendedor();
    infVendedor.nome_vendedor = this.formVendedor.value.nome_vendedor
    infVendedor.login = this.formVendedor.value.login
    infVendedor.senha = this.formVendedor.value.senha
    infVendedor.ativo = this.formVendedor.value.ativo

    this.vendedorService.createVendedor(infVendedor)
    .pipe(first()).subscribe(result => {
      this.alertService.success(`Vendedor ${infVendedor.nome_vendedor} criada com sucesso`);
      this.vendedor = result;
      document.getElementById('closeAddModal').click();
    }, error => {
      this.alertService.error(error);
      document.getElementById('closeAddModal').click();
      this.loading = false;
    })
  }

  clean(): void {
    this.submitted = false;
    this.loading = false;
  }

  getStatus(status: boolean): string {
    if (status) {
      return "Ativo"
    }
    return "Inativo"
  }
}
