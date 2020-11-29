import { Pedido } from './../models/pedido.model.model';
import { Produto } from './../models/produto.model';
import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {API_URL} from '../env';


@Injectable({ providedIn: 'root' })
export class PedidoService {

  constructor(private http: HttpClient) {}

  getAll() {
    return this.http.get<any>(`${API_URL}/pedidos`);
  }

  getById(id: number) {
    return this.http.get<Pedido>(`${API_URL}/pedidos/${id}`);
  }

  putPedido(pedido: Pedido, id: number) {
    return this.http.put<Pedido>(`${API_URL}/pedidos/${id}`, pedido);
  }

  deletePedido(id: number) {
    return this.http.delete(`${API_URL}/pedidos/${id}`);
  }

  createPedido(pedido: Pedido) {
    return this.http.post<Pedido>(`${API_URL}/pedidos/cadastro`, pedido);
  }
}