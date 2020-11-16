import { Categoria } from './../models/categoria.model';
import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {API_URL} from '../env';

@Injectable({ providedIn: 'root' })
export class CategoriaService {

  constructor(private http: HttpClient) {

  }

  getAll() {
    return this.http.get<any>(`${API_URL}/categorias`);
  }

  getById(id: number) {
    return this.http.get(`${API_URL}/categorias/${id}`);
  }

  putCategoria(categoria: Categoria) {
    return this.http.put<Categoria>(
      `${API_URL}/categorias/${categoria.cod_categoria}`, 
      { nome_categoria: categoria.nome_categoria });
  }

  deleteCategoria(id: number) {
    return this.http.delete(`${API_URL}/categorias/${id}`);
  }

  createCategoria(categoria: Categoria) {
    return this.http.post<Categoria>(`${API_URL}/categorias/cadastro`, { nome_categoria: categoria.nome_categoria });
  }
}