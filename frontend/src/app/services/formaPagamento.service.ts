import { FormaPagamento } from './../models/formaPagamento.model';
import { Categoria } from './../models/categoria.model';
import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {API_URL} from '../env';

@Injectable({ providedIn: 'root' })
export class FormaPagamentoService {

  constructor(private http: HttpClient) {}

  getAll() {
    return this.http.get<any>(`${API_URL}/formas-de-pagamento`);
  }

  getById(id: number) {
    return this.http.get(`${API_URL}/forma-de-pagamento/${id}`);
  }

  putFormaPagamento(formaPagamento: FormaPagamento) {
    return this.http.put<Categoria>(
      `${API_URL}/forma-de-pagamento/${formaPagamento.cod_formaPgameno}`, 
      { tipo_formaPagamento: formaPagamento.tipo_formaPagamento,
        descricao_formaPagamento: formaPagamento.descricao_formaPagamento });
  }

  deleteFormaPagamento(id: number) {
    return this.http.delete(`${API_URL}/forma-de-pagamento/${id}`);
  }

  createFormaPagamento(formaPagamento: FormaPagamento) {
    return this.http.post<FormaPagamento>(
        `${API_URL}/forma-de-pagamento/cadastro`, 
        { tipo_formaPagamento: formaPagamento.tipo_formaPagamento,
          descricao_formaPagamento: formaPagamento.descricao_formaPagamento });
  }
}