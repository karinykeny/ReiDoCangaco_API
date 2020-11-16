import { API_URL } from './../env';
import { Login } from './../models/login.model';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';


@Injectable({ providedIn: 'root' })
export class AuthenticationService {
    private currentUserSubject: BehaviorSubject<Login>;
    public currentUser: Observable<Login>;

    constructor(private http: HttpClient) {
        this.currentUserSubject = new BehaviorSubject<Login>(JSON.parse(localStorage.getItem('access_token')));
        this.currentUser = this.currentUserSubject.asObservable();
    }

    public get currentUserValue(): Login {
        return this.currentUserSubject.value;
    }

    login(login: Login) {
        return this.http.post<any>(`${API_URL}/login`, login)
        .pipe(map(access_token => {
            localStorage.setItem('token', JSON.stringify(access_token));
            this.currentUserSubject.next(access_token);
            return access_token;
        }));
    }

    logout() {
        localStorage.removeItem('token');
        this.currentUserSubject.next(null);
    }
}