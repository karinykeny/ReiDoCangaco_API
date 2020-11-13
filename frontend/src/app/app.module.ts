import { VendedorService } from './services/vendedor.service';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { ReactiveFormsModule } from '@angular/forms';
import { AlertaComponent } from './alerta/alerta.component';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { AuthenticationService } from './services/authentication.service';
import { AlertService } from './services/alert.service';
import { JwtInterceptor } from './helpers/jwt.interceptor';
import { ErrorInterceptor } from './helpers/error.interceptor';
import { VendedorCadastroComponent } from './pages/vendedor-cadastro/vendedor-cadastro.component';
import { VendedorListComponent } from './pages/vendedor-list/vendedor-list.component';
import { VendaComponent } from './pages/venda/venda.component';
import { PedidosComponent } from './pages/pedidos/pedidos.component';
import { FornecedorCadastroComponent } from './pages/fornecedor-cadastro/fornecedor-cadastro.component';
import { FornecedorListComponent } from './pages/fornecedor-list/fornecedor-list.component';
import { FormaPagamentoCadastroComponent } from './pages/forma-pagamento-cadastro/forma-pagamento-cadastro.component';
import { FormaPagamentoListComponent } from './pages/forma-pagamento-list/forma-pagamento-list.component';
import { CategoriaCadastroComponent } from './pages/categoria-cadastro/categoria-cadastro.component';
import { CategoriaListComponent } from './pages/categoria-list/categoria-list.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    HomeComponent,
    AlertaComponent,
    VendedorCadastroComponent,
    VendedorListComponent,
    VendaComponent,
    PedidosComponent,
    FornecedorCadastroComponent,
    FornecedorListComponent,
    FormaPagamentoCadastroComponent,
    FormaPagamentoListComponent,
    CategoriaCadastroComponent,
    CategoriaListComponent
  ],
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    HttpClientModule, 
    AppRoutingModule
  ],
  providers: [
    VendedorService, 
    AuthenticationService, 
    AlertService,
    { provide: HTTP_INTERCEPTORS, useClass: JwtInterceptor, multi: true },
    { provide: HTTP_INTERCEPTORS, useClass: ErrorInterceptor, multi: true },
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
