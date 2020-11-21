
import { Categoria } from './../../models/categoria.model';
import { Component, OnInit } from '@angular/core';
import { CategoriaService } from 'src/app/services/categoria.service';
import { AlertService } from 'src/app/services/alert.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-categoria-list',
  templateUrl: './categoria-list.component.html',
  styleUrls: ['./categoria-list.component.css']
})
export class CategoriaListComponent implements OnInit {

  categorias = new Array<Categoria>();
  categorias_db = new Array<Categoria>();
  categoriaEdit: Categoria = new Categoria();
  formCategoria: FormGroup;
  loading = false;
  submitted = false;
  public paginaAtual = 1;

  constructor(
    private categoriaService: CategoriaService,
    private alertService: AlertService,
    private formBuilder: FormBuilder,
    ) { }

  ngOnInit(): void {
    this.createForm(new Categoria());
    this.getCategorias();
    this.categorias = this.categorias_db;
  }

  createForm(categoria: Categoria) {
    this.formCategoria = this.formBuilder.group({
      nome_categoria: [categoria.nome_categoria, this.categoriaEdit.cod_categoria ? Validators.required : Validators.nullValidator ]
    })
  }

  getCategorias(): void {
    this.categoriaService.getAll().subscribe(
      result => {
        this.categorias_db = result.categorias;
        this.categorias = this.categorias_db;
    });
  }

  getEditModal(categoria: Categoria): void {
    this.categoriaEdit = categoria;
  }

  getAddModal(): void {
    this.categoriaEdit = null;
  }

  getDeleteModal(categoria: Categoria): void {
    this.categoriaEdit = categoria;
  }

  get fc() { return this.formCategoria.controls; }

  saveCategoria(): void {
    this.submitted = true;
    this.alertService.clear();
    if (this.formCategoria.invalid) { 
      return; 
    }
    this.loading = true;

    const newCategoria = new Categoria();
    newCategoria.nome_categoria = this.formCategoria.value.nome_categoria

    this.categoriaService.createCategoria(newCategoria)
    .pipe(first()).subscribe(result => {
      this.alertService.success("Categoria criada com sucesso");
      this.getCategorias();
      document.getElementById('closeAddModal').click();
    }, error => {
      this.alertService.error(error.error.mensagem);
      document.getElementById('closeAddModal').click();
      this.loading = false;
    })
  }


  editCategoria(): void {
    this.submitted = true;
    this.alertService.clear();
    if (this.formCategoria.invalid) { 
      return; 
    }
    this.loading = true; 

    const infCategoria = new Categoria();
    infCategoria.cod_categoria = this.categoriaEdit.cod_categoria
    infCategoria.nome_categoria = this.formCategoria.value.nome_categoria

    this.categoriaService.putCategoria(infCategoria)
    .pipe(first()).subscribe( reult => {
      this.alertService.success(`Categoria com código ${infCategoria.cod_categoria} foi alterada`);
      this.getCategorias();
      document.getElementById('closeModal').click();
    }, error => {
      this.alertService.error(error.error.mensagem);
      document.getElementById('closeModal').click();
      this.loading = false;
    })
  }

  deleteCategoria(): void {
    this.alertService.clear();
    this.loading = true;

    this.categoriaService.deleteCategoria(this.categoriaEdit.cod_categoria)
    .pipe(first()).subscribe( result => {
      this.alertService.success("Categoria excluída com sucesso");
      this.getCategorias();
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

  filtrar(value: any) {
    if(!value) {
      this.categorias = this.categorias_db;
   } else {
     this.categorias = this.categorias_db.filter( categoria => 
      categoria.nome_categoria.trim().toLowerCase().includes(value.trim().toLowerCase())
     );
   }
  }
  
}
