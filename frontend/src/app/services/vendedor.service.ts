import { AccessToken } from './../types/access-token';
import { Vendedor } from './../model/vendedor.model';
import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {API_URL} from '../env';
import { Login } from '../types/login';

@Injectable()
export class VendedorService {

  token: AccessToken = {access_token: ""};
  headers = new HttpHeaders().set('Authorization', `Bearer ${this.token.access_token}`);

  constructor(private http: HttpClient) {
  }

  getVendedor(id: number) {
    this.http.get(`${API_URL}/usuarios/${id}`).subscribe(
      consulta => {
        return consulta;
      }
    )
  }

  getVendedores() {
    this.http.get(`${API_URL}/usuarios`).subscribe(
      consulta => { 
        return consulta
      }
    )
  }

  login(login: Login) {
    this.http.post<AccessToken>(`${API_URL}/login`, JSON.stringify(login)).subscribe(
      consulta => {
        return this.token = consulta;
      }
    );
  }

  cadastro(vendedor: Vendedor) {
    this.http.post<Vendedor>(`${API_URL}/cadastro`, JSON.stringify(vendedor))
    .subscribe(consulta => {
        return consulta;
      }
    );
  }

  logout() {
    this.http.post(`${API_URL}/logout`, this.headers).subscribe(
      consulta => {
        return consulta;
      }
    );
  }


  
}