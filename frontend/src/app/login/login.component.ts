import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { first } from 'rxjs/operators';
import { Login } from '../models/login.model';
import { AlertService } from '../services/alert.service';
import { AuthenticationService } from '../services/authentication.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  formLogin: FormGroup;
  loading = false;
  submitted = false;
  returnUrl: any;

  constructor(private formBuilder: FormBuilder,
              private route: ActivatedRoute,
              private authenticationService: AuthenticationService,
              private alertService: AlertService,
              private router: Router) { 
    if (this.authenticationService.currentUserValue) {
      this.router.navigate(['/']);
    }
  }

  ngOnInit() {
    this.createForm(new Login());
    this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
  }

  createForm(login: Login) {
    this.formLogin = this.formBuilder.group({
      login: [login.login, Validators.required],
      senha: [login.senha, Validators.required]
    })
  }

  get f() { return this.formLogin.controls; }

  onSubmit() {
    this.submitted = true;
    this.alertService.clear();

    if (this.formLogin.invalid) {
      return;
    }

    this.loading = true;
    this.authenticationService.login(this.formLogin.value)
      .pipe(first())
      .subscribe(
        () => {
          return this.router.navigate([this.returnUrl]);
        },
        error => {
          this.alertService.error(error.error.mensagem);
          this.loading = false;
      });
  }
  
}
