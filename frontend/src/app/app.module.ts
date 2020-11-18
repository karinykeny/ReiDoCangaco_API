import { VendedorService } from './services/vendedor.service';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
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
import { FormaPagamentoListComponent } from './pages/forma-pagamento-list/forma-pagamento-list.component';
import { CategoriaListComponent } from './pages/categoria-list/categoria-list.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {TableModule} from 'primeng/table';
import {ToastModule} from 'primeng/toast';
import {CalendarModule} from 'primeng/calendar';
import {SliderModule} from 'primeng/slider';
import {MultiSelectModule} from 'primeng/multiselect';
import {ContextMenuModule} from 'primeng/contextmenu';
import {DialogModule} from 'primeng/dialog';
import {ButtonModule} from 'primeng/button';
import {DropdownModule} from 'primeng/dropdown';
import {ProgressBarModule} from 'primeng/progressbar';
import {InputTextModule} from 'primeng/inputtext';
import {FileUploadModule} from 'primeng/fileupload';
import {ToolbarModule} from 'primeng/toolbar';
import {RatingModule} from 'primeng/rating';
import {RadioButtonModule} from 'primeng/radiobutton';
import { ConfirmDialogModule } from 'primeng/confirmdialog';
import {PasswordModule} from 'primeng/password';
import { ConfirmationService, MessageService } from 'primeng/api';
import { CategoriaService } from './services/categoria.service';
import { NgxPaginationModule } from 'ngx-pagination';
import { FormaPagamentoService } from './services/formaPagamento.service';
import { HomeBodyComponent } from './pages/home-body/home-body.component';
import { FornecedorService } from './services/fornecedor.service';

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
    FormaPagamentoListComponent,
    CategoriaListComponent,
    HomeBodyComponent,
  ],
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    HttpClientModule,
    NgxPaginationModule,
    BrowserAnimationsModule,
    TableModule,
    AppRoutingModule,
    CalendarModule,
		SliderModule,
		DialogModule,
		MultiSelectModule,
		ContextMenuModule,
		DropdownModule,
		ButtonModule,
		ToastModule,
    InputTextModule,
    ProgressBarModule,
    FileUploadModule,
    ToolbarModule,
    RatingModule,
    FormsModule,
    RadioButtonModule,
    ConfirmDialogModule,
    PasswordModule,
    FormsModule
  ],
  providers: [
    VendedorService,
    CategoriaService,
    FormaPagamentoService,
    FornecedorService,
    AuthenticationService, 
    AlertService,
    ConfirmationService,
    MessageService,
    { provide: HTTP_INTERCEPTORS, useClass: JwtInterceptor, multi: true },
    { provide: HTTP_INTERCEPTORS, useClass: ErrorInterceptor, multi: true },
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
