import { VendedorService } from './../../services/vendedor.service';
import { Vendedor } from './../../models/vendedor.model';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AlertService } from 'src/app/services/alert.service';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-vendedor-list',
  templateUrl: './vendedor-list.component.html',
  styleUrls: ['./vendedor-list.component.scss']
})
export class VendedorListComponent implements OnInit {
  vendedores = new Array<Vendedor>();
  vendedores_db = new Array<Vendedor>();
  vendedorEdit: Vendedor = new Vendedor();
  formVendedor: FormGroup;
  id: number;
  loading = false;
  submitted = false;
  public paginaAtual = 1;
  statusList = ["Ativo","Inativo"]

  constructor(
    private vendedorService: VendedorService,
    private alertService: AlertService,
    private formBuilder: FormBuilder,
    ) { }

  ngOnInit(): void {
    this.createForm(new Vendedor());
    this.getVendedores();
  }

  getIsAddMode(): void {
    if (this.vendedorEdit.cod_vendedor) {
      this.id = this.vendedorEdit.cod_vendedor;
      this.vendedorService.getById(this.id)
        .pipe(first()).subscribe(x => {
          this.formVendedor.patchValue(x);
        });
    }
  }

  createForm(vendedor: Vendedor) {
    this.formVendedor = this.formBuilder.group({
      nome_vendedor: [vendedor.nome_vendedor, [Validators.required, Validators.minLength(3), Validators.maxLength(150)]],
      login: [vendedor.login, [Validators.required, Validators.minLength(3), Validators.maxLength(50)]],
      senha: [vendedor.senha, [Validators.required, Validators.minLength(3), Validators.maxLength(50)]],
      ativo: [vendedor.ativo, Validators.required],
    })
  }

  getVendedores(): void {
    this.vendedorService.getAll().subscribe(
      result => {
        this.vendedores = result.vendedores;
        this.vendedores_db = result.vendedores;
    });
  }

  getInfModal(vendedor: Vendedor): void {
    this.vendedorEdit = vendedor;
  }

  get v() { return this.formVendedor.controls; }


  editVendedor(): void {
    this.submitted = true;
    this.alertService.clear();
    if (this.formVendedor.invalid) { 
      return; 
    }
    this.loading = true; 

    const infVendedor = new Vendedor();
    infVendedor.cod_vendedor = this.id;
    infVendedor.nome_vendedor = this.formVendedor.value.nome_vendedor;
    infVendedor.login = this.formVendedor.value.login;
    infVendedor.senha = this.formVendedor.value.senha;
    infVendedor.ativo = this.formVendedor.value.ativo;

    this.vendedorService.putVendedor(infVendedor)
    .pipe(first()).subscribe( reult => {
      this.alertService.success(`Vendedor com código ${infVendedor.cod_vendedor} foi alterada`);
      this.getVendedores();
      document.getElementById('closeModal').click();
    }, error => {
      this.alertService.error(error);
      document.getElementById('closeModal').click();
      this.loading = false;
    })
  }

  deleteVendedor(): void {
    this.alertService.clear();
    this.loading = true;

    this.vendedorService.deleteById(this.vendedorEdit.cod_vendedor)
    .pipe(first()).subscribe( result => {
      this.alertService.success("Vendedor excluído com sucesso");
      this.getVendedores();
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
      this.vendedores = this.vendedores_db;
   } else {
     this.vendedores = this.vendedores_db.filter( vendedor => 
      vendedor.nome_vendedor.trim().toLowerCase().includes(value.trim().toLowerCase())
     );
   }
  }

  getStatus(status: boolean): string {
    if (status) {
      return "Ativo"
    }
    return "Inativo"
  }
}
