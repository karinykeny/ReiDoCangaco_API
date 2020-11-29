import { ProdutoService } from './../../services/produto.service';
import { Produto } from './../../models/produto.model';
import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from 'src/app/services/authentication.service';
import { Login } from 'src/app/models/login.model';
import { AlertService } from 'src/app/services/alert.service';
import { FormBuilder, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-venda',
  templateUrl: './venda.component.html',
  styleUrls: ['./venda.component.css']
})
export class VendaComponent implements OnInit {
  formProduto: FormGroup;
  produto = new Produto();
  vendedor: string;
  total: number = 13.5;
  qtd_itens: number = 9;
  cod: string;
  qtd_produto = 1;
  valorTotal = 0;
  currentUser: Login;
  
  produtos = new Array<Produto>();
  produtos_db = new Array<Produto>();
  itens = [
    {qtd_produto: 3, nome_produto: "Banana", valor_produto: 1.5, valor_compra: 4.5},
    {qtd_produto: 3, nome_produto: "Banana", valor_produto: 1.5, valor_compra: 4.5},
    {qtd_produto: 3, nome_produto: "Banana", valor_produto: 1.5, valor_compra: 4.5}
  ];
  data = new Date();

  constructor(
    private produtoService: ProdutoService,
    private authenticationService: AuthenticationService,
    private alertService: AlertService,
    private formBuilder: FormBuilder,
  ) { }
    

  ngOnInit(): void {
    this.getProdutos();
    this.authenticationService.currentUser.subscribe(x => {
      this.currentUser = x;
    });
  }

  createForm(produto: Produto) {
    this.formProduto = this.formBuilder.group({
      cod_produto: [produto.cod_produto],
      nome_produto: [produto.nome_produto],
      valor_produto: [produto.valor_produto],
      ativo: [produto.ativo],
      cod_categoria: [produto.cod_categoria],
      cod_fornecedor: [produto.cod_fornecedor]
    })
  }

  getProdutos(): void {
    this.produtoService.getAll().subscribe( result => {
      this.produtos = result.produtos;
      this.produtos_db = result.produtos;
    })
  }

  getTotal(): number {
    let total = 0;
    for (let item of this.itens) {
      total = total + item.valor_compra;
    }
    return total;
  }

  getQtdItens(): number {
    let qtd = 0;
    for (let item of this.itens) {
      qtd = qtd + item.qtd_produto;
    }
    return qtd;
  }duto

  getProduto(): void {
    for (let produto of this.produtos) {
      if (this.cod === produto.cod_produto) {
        this.produto = produto;
        this.valorTotal = produto.valor_produto * this.qtd_produto;
      }
    }
  }

  quantidade(qtd: any) {
    if(qtd) {
      this.qtd_produto = qtd;
    }
  }

  setProduto(cod: any) {
    if(cod) {
      this.cod = cod;
    }
  }
}
