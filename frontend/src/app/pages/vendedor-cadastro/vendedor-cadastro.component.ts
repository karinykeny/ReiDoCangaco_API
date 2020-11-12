import { Vendedor } from './../../models/vendedor.model';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-vendedor-cadastro',
  templateUrl: './vendedor-cadastro.component.html',
  styleUrls: ['./vendedor-cadastro.component.css']
})
export class VendedorCadastroComponent implements OnInit {
  formVendedor: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
  ) { }

  ngOnInit(): void {
    this.createForm(new Vendedor());
  }

  createForm(vendedor: Vendedor) {
    this.formVendedor = this.formBuilder.group({
      nome_vendedor: [vendedor.nome_vendedor, Validators.required],
      login: [vendedor.login, Validators.required],
      senha: [vendedor.senha, Validators.required],
      ativo: [vendedor.ativo]
    })
  }

  onSubmit() {

  }
}
