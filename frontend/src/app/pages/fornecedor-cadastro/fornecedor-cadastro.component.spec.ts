import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FornecedorCadastroComponent } from './fornecedor-cadastro.component';

describe('FornecedorCadastroComponent', () => {
  let component: FornecedorCadastroComponent;
  let fixture: ComponentFixture<FornecedorCadastroComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FornecedorCadastroComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(FornecedorCadastroComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
