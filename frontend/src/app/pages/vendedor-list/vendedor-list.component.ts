import { VendedorService } from './../../services/vendedor.service';
import { Vendedor } from './../../models/vendedor.model';
import { Component, OnInit } from '@angular/core';
import { ConfirmationService, MessageService } from 'primeng/api';
import { first } from 'rxjs/operators';


@Component({
  selector: 'app-vendedor-list',
  templateUrl: './vendedor-list.component.html',
  styles: [`
  :host ::ng-deep .p-dialog .product-image {
      width: 150px;
      margin: 0 auto 2rem auto;
      display: block;
  }
`],
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
    private confirmationService: ConfirmationService,
    private messageService: MessageService
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
    this.confirmationService.confirm({
        message: 'Tem certeza de que deseja excluir os vendedores selecionados?',
        header: 'Confirm',
        icon: 'pi pi-exclamation-triangle',
        accept: () => {
            this.vendedores = this.vendedores.filter(val => !this.selecioneVendedores.includes(val));
            for(let vendedor of this.vendedores) {
              this.vendedorService.deleteById(vendedor.cod_vendedor).subscribe(
                result => {
                  this.vendedor;
                  this.messageService.add({severity:'success', summary: 'Successful', detail: 'Vendedor excluído', life: 3000});
              })
            }
            this.selecioneVendedores = null;
            this.messageService.add({severity:'success', summary: 'Successful', detail: 'Products Deleted', life: 3000});
        }
    });
  }

  editVendedor(vendedor: Vendedor) {
      this.vendedor = {...vendedor};
      this.vendedorDialog = true;
  }

  deleteVendedor(vendedor: Vendedor) {
    this.confirmationService.confirm({
      message: 'Tem certeza de que deseja excluir o vendedor ' + vendedor.nome_vendedor + '?',
      header: 'Confirm',
      icon: 'pi pi-exclamation-triangle',
      accept: () => {
        this.vendedorService.deleteById(vendedor.cod_vendedor).subscribe(
          result => {
            this.vendedor;
            this.messageService.add({severity:'success', summary: 'Successful', detail: 'Vendedor excluído', life: 3000});
          }
      )}
    });
  }

  hideDialog() {
    this.vendedorDialog = false;
    this.submitted = false;
  }

  saveVendedor() {
    this.submitted = true;

    if (this.vendedor.nome_vendedor.trim()) {
      if (this.vendedor.cod_vendedor) {
        this.vendedorService.putVendedor(this.vendedor).subscribe(
          result => {
            this.vendedor = result; 
            this.messageService.add({severity:'success', summary: 'Successful', detail: 'Product Updated', life: 3000});
        });
      }
      this.vendedores = [...this.vendedores];
      this.vendedorDialog = false;
      this.vendedor;
    }                
  }

  findIndexById(id: number): number {
    let index = -1;
    for (let i = 0; i < this.vendedores.length; i++) {
      if (this.vendedores[i].cod_vendedor === id) {
        index = i;
        break;
      }
    }
    return index;
  }

  createId(): string {
    let id = '';
    var chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    for ( var i = 0; i < 5; i++ ) {
        id += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return id;
  }

  getStatus(status: boolean): string {
    switch(status) {
      case true:
        return "Ativo";
      case false:
        return "Inativo";
      default:
        return ""
    }
  }
}
