import { Produto } from './../models/produto.model';
import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {API_URL} from '../env';


@Injectable({ providedIn: 'root' })
export class ProdutoService {

  constructor(private http: HttpClient) {}

  getAll() {
    return this.http.get<any>(`${API_URL}/produtos`);
  }

  getById(id: number) {
    return this.http.get<Produto>(`${API_URL}/produtos/${id}`);
  }

  putProduto(produto: Produto, id: number) {
    return this.http.put<Produto>(`${API_URL}/produtos/${id}`, produto);
  }

  deleteProduto(id: number) {
    return this.http.delete(`${API_URL}/produtos/${id}`);
  }

  createProduto(produto: Produto) {
    return this.http.post<Produto>(`${API_URL}/produtos/cadastro`, produto);
  }
}