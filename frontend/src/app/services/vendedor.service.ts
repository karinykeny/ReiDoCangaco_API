import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {API_URL} from '../env';
import { Vendedor } from '../models/vendedor.model';

@Injectable({ providedIn: 'root' })
export class VendedorService {

  constructor(private http: HttpClient) {
  }

  getAll() {
    return this.http.get<any>(`${API_URL}/usuarios`);
  }

  getById(id: number) {
    return this.http.get(`${API_URL}/usuarios/${id}`);
  }

  putVendedor(vendedor: Vendedor) {
    return this.http.put<Vendedor>(`${API_URL}/usuarios/${vendedor.cod_vendedor}`, vendedor);
  }

  deleteById(id: number) {
    return this.http.delete(`${API_URL}/usuarios/${id}`);
  }

  createVendedor(vendedor: Vendedor) {
    return this.http.post<Vendedor>(`${API_URL}/cadastro`, vendedor);
  }
}