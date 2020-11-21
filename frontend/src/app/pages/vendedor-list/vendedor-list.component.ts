import { VendedorService } from './../../services/vendedor.service';
import { Vendedor } from './../../models/vendedor.model';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-vendedor-list',
  templateUrl: './vendedor-list.component.html',
  styleUrls: ['./vendedor-list.component.scss']
})
export class VendedorListComponent implements OnInit {
  vendedorDialog: boolean;
  vendedores: Vendedor[];
  vendedor: Vendedor;
  selecioneVendedores: Vendedor[];
  submitted: boolean;
  delete = "Excluir";

  constructor(
    private vendedorService: VendedorService,
    ) { }

  ngOnInit(): void {
    this.vendedorService.getAll()
    .then(data => this.vendedores = data);
  }

  openNew() {
    this.vendedor;
    this.submitted = false;
    this.vendedorDialog = true;
  }

  deleteSelectedVendedores() {
    
  }

  editVendedor(vendedor: Vendedor) {
      this.vendedor = {...vendedor};
      this.vendedorDialog = true;
  }

  deleteVendedor(vendedor: Vendedor) {
    
  }

  hideDialog() {
    this.vendedorDialog = false;
    this.submitted = false;
  }

  saveVendedor() {
        
  }

  
}
