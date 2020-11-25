import { ProdutoService } from './../../services/produto.service';
import { Produto } from './../../models/produto.model';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-venda',
  templateUrl: './venda.component.html',
  styleUrls: ['./venda.component.css']
})
export class VendaComponent implements OnInit {
  vendedor: string = "Kariny Keny"
  total: number = 13.5;
  qtd_itens: number = 9;
  produto = new Produto();
  produtos = new Array<Produto>();
  itens = [
    {qtd_produto: 3, nome_produto: "Banana", valor_produto: 1.5, valor_compra: 4.5},
    {qtd_produto: 3, nome_produto: "Banana", valor_produto: 1.5, valor_compra: 4.5},
    {qtd_produto: 3, nome_produto: "Banana", valor_produto: 1.5, valor_compra: 4.5}
  ];

  constructor(
    private produtoService: ProdutoService
  ) { }

  ngOnInit(): void {
    this.getProdutos();
  }

  getProdutos(): void {
    this.produtoService.getAll().subscribe( result => {
      this.produtos = result.produtos;
    })
  }

}
