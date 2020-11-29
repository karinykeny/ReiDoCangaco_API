import { CategoriaService } from 'src/app/services/categoria.service';
import { FornecedorService } from './../../services/fornecedor.service';
import { Fornecedor } from 'src/app/models/fornecedor.model';
import { ProdutoService } from './../../services/produto.service';
import { Produto } from './../../models/produto.model';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AlertService } from 'src/app/services/alert.service';
import { first } from 'rxjs/operators';
import { Categoria } from 'src/app/models/categoria.model';

@Component({
  selector: 'app-produto-list',
  templateUrl: './produto-list.component.html',
  styleUrls: ['./produto-list.component.css']
})
export class ProdutoListComponent implements OnInit {

  produtos = new Array<Produto>();
  produtos_db = new Array<Produto>();
  categorias = new Array<Categoria>();
  fornecedores = new Array<Fornecedor>();
  produtoEdit: Produto = new Produto();
  categoria: Categoria;
  fornecedor: Fornecedor;
  formProduto: FormGroup;
  ativosList = ["Sim","Não"];
  isAddMode: boolean;
  id: number;
  loading = false;
  submitted = false;
  public paginaAtual = 1;


  constructor(
    private produtoService: ProdutoService,
    private fornacedorService: FornecedorService,
    private categoriaService: CategoriaService,
    private alertService: AlertService,
    private formBuilder: FormBuilder,
    ) { }

  ngOnInit(): void {
    this.createForm(new Produto());
    this.getFornecedores();
    this.getCategorias();
    this.getProdutos();
  }

  getIsAddMode(): void {
    if (this.produtoEdit.id_produto) {
      this.id = this.produtoEdit.id_produto;
      this.produtoService.getById(this.id)
        .pipe(first()).subscribe(x => {
          this.formProduto.patchValue(x);
          this.isAddMode = false;
        });
    }
  }

  getAddMode(): void {
    this.isAddMode = true;
    this.formProduto.reset();
  }

  createForm(produto: Produto) {
    this.formProduto = this.formBuilder.group({
      cod_produto: [produto.cod_produto, [Validators.required, Validators.minLength(1), Validators.maxLength(50)]],
      nome_produto: [produto.nome_produto, [Validators.required, Validators.minLength(3), Validators.maxLength(150)]],
      valor_produto: [produto.valor_produto, [Validators.required, Validators.minLength(2)]],
      ativo: [produto.ativo, [Validators.required, Validators.minLength(3), Validators.maxLength(3)]],
      cod_categoria: [produto.cod_categoria, Validators.required],
      cod_fornecedor: [produto.cod_fornecedor, Validators.required]
    })
  }

  getProdutos(): void {
    this.produtoService.getAll().subscribe(
      result => {
        this.produtos_db = result.produtos;
        this.produtos = this.produtos_db;
    });
  }

  getFornecedores(): void {
    this.fornacedorService.getAll().subscribe(
      result => {
        this.fornecedores = result.fornecedores;
    });
  }

  getCategorias(): void {
    this.categoriaService.getAll().subscribe(
      result => {
        this.categorias = result.categorias;
    });
  }

  getInfModal(produto: Produto): void {
    this.produtoEdit = produto;
  }

  get p() { return this.formProduto.controls; }

  onSubmit() {
    this.submitted = true;
    this.alertService.clear();
    if (this.formProduto.invalid) {
        return;
    }

    this.loading = true;

    if (this.isAddMode) {
        this.saveProduto();
    } else {
        this.editProduto();
    }
  }

  saveProduto(): void {
    this.produtoService.createProduto(this.formProduto.value)
    .pipe(first()).subscribe(() => {
      this.alertService.success(`Produto ${this.formProduto.value.nome_produto} criada com sucesso`);
      this.getProdutos();
      document.getElementById('closeAddModal').click();
    }, error => {
      this.alertService.error(error);
      document.getElementById('closeAddModal').click();
      this.loading = false;
    })
  }


  editProduto(): void {
    this.produtoService.putProduto(this.formProduto.value, this.id)
    .pipe(first()).subscribe(() => {
      this.alertService.success(`Produto com código ${this.formProduto.value.cod_produto} foi alterada`);
      this.getProdutos();
      document.getElementById('closeModal').click();
    }, error => {
      this.alertService.error(error);
      document.getElementById('closeModal').click();
      this.loading = false;
    })
  }

  deleteCategoria(): void {
    this.alertService.clear();
    this.loading = true;

    this.produtoService.deleteProduto(this.produtoEdit.id_produto)
    .pipe(first()).subscribe( result => {
      this.alertService.success("Produto excluído com sucesso");
      this.getProdutos();
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
      this.produtos = this.produtos_db;
   } else {
     this.produtos = this.produtos_db.filter( produto => 
      produto.nome_produto.trim().toLowerCase().includes(value.trim().toLowerCase())
     );
   }
  }

  getFornecedor(id: number): String {
    for(let fornecedor of this.fornecedores) {
      if(fornecedor.cod_fornecedor === id) {
        return fornecedor.nome_fantasia;
      }
    }
    return "";
  }

  getCategoria(id: number): String {
    for(let categoria of this.categorias) {
      if (categoria.cod_categoria === id) {
        return categoria.nome_categoria;
      }
    }
    return "";
  }
}
