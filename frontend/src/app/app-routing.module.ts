import { ProdutoListComponent } from './pages/produto-list/produto-list.component';
import { HomeBodyComponent } from './pages/home-body/home-body.component';
import { CategoriaListComponent } from './pages/categoria-list/categoria-list.component';
import { FornecedorListComponent } from './pages/fornecedor-list/fornecedor-list.component';
import { FornecedorCadastroComponent } from './pages/fornecedor-cadastro/fornecedor-cadastro.component';
import { PedidosComponent } from './pages/pedidos/pedidos.component';
import { VendaComponent } from './pages/venda/venda.component';
import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AuthGuard } from './helpers/auth.guard';
import { VendedorCadastroComponent } from './pages/vendedor-cadastro/vendedor-cadastro.component';
import { VendedorListComponent } from './pages/vendedor-list/vendedor-list.component';
import { FormaPagamentoListComponent } from './pages/forma-pagamento-list/forma-pagamento-list.component';

const routes: Routes = [
  {path: '', 
  component: HomeComponent, 
  canActivate: [AuthGuard],
  children: [
    {
      path: '',
      component: HomeBodyComponent,
      canActivate: [AuthGuard]
    },
    {
      path: 'venda',
      component: VendaComponent,
      canActivate: [AuthGuard]
    },
    {
      path: 'pedidos',
      component: PedidosComponent,
      canActivate: [AuthGuard]
    },
    {
        path: 'vendedor-cadastro',
        component: VendedorCadastroComponent,
        canActivate: [AuthGuard]
    },
    {
        path: 'vendedor-lista',
        component: VendedorListComponent,
        canActivate: [AuthGuard]
    },
    {
      path: 'fornecedor-cadastro',
      component: FornecedorCadastroComponent,
      canActivate: [AuthGuard]
    },
    {
      path: 'fornecedor-lista',
      component: FornecedorListComponent,
      canActivate: [AuthGuard]
    },
    {
      path: 'forma-pagamento-lista',
      component: FormaPagamentoListComponent,
      canActivate: [AuthGuard]
    },
    {
      path: 'categoria-lista',
      component: CategoriaListComponent,
      canActivate: [AuthGuard]
    },
    {
      path: 'produto-lista',
      component: ProdutoListComponent,
      canActivate: [AuthGuard]
    }
  ]
},
  {path: 'login', component: LoginComponent},
  { path: '**', redirectTo: '' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
