import { Contato } from './../models/contato.model';
import { Fornecedor } from './../models/fornecedor.model';
import { FormaPagamento } from './../models/formaPagamento.model';
import { Categoria } from './../models/categoria.model';
import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {API_URL} from '../env';
import { NumberFormatStyle } from '@angular/common';

@Injectable({ providedIn: 'root' })
export class ContatoService {

  constructor(private http: HttpClient) {}

  getAll() {
    return this.http.get<any>(`${API_URL}/contatos`);
  }

  getById(id: number) {
    return this.http.get(`${API_URL}/contato/${id}`);
  }

  putContato(contato: Contato, id: number) {
    return this.http.put<Contato>(
      `${API_URL}/contato/${id}`, contato);
  }

  deleteContato(id: number) {
    return this.http.delete(`${API_URL}/contato/${id}`);
  }

  createContato(contato: Contato) {
    return this.http.post<Contato>(`${API_URL}/contato/cadastro`, contato);
  }
}