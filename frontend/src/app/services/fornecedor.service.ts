import { Fornecedor } from './../models/fornecedor.model';
import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {API_URL} from '../env';

@Injectable({ providedIn: 'root' })
export class FornecedorService {

  constructor(private http: HttpClient) {}

  getAll() {
    return this.http.get<any>(`${API_URL}/fornecedores`);
  }

  getById(id: number) {
    return this.http.get(`${API_URL}/fornecedores/${id}`);
  }

  putFornecedor(fornecedor: Fornecedor) {
    return this.http.put<Fornecedor>(
      `${API_URL}/fornecedores/${fornecedor.cod_fornecedor}`, { 
        cnpj_cpf: fornecedor.cnpj_cpf,
        nome_fantasia: fornecedor.nome_fantasia,
        razao_social: fornecedor.razao_social,
        ativo: fornecedor.ativo});
  }

  deleteFornecedor(id: number) {
    return this.http.delete(`${API_URL}/fornecedores/${id}`);
  }

  createFornecedor(fornecedor: Fornecedor) {
    return this.http.post<Fornecedor>(
        `${API_URL}/fornecedores/cadastro`,{ 
            cnpj_cpf: fornecedor.cnpj_cpf,
            nome_fantasia: fornecedor.nome_fantasia,
            razao_social: fornecedor.razao_social,
            ativo: fornecedor.ativo});
  }
}