import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FormaPagamentoCadastroComponent } from './forma-pagamento-cadastro.component';

describe('FormaPagamentoCadastroComponent', () => {
  let component: FormaPagamentoCadastroComponent;
  let fixture: ComponentFixture<FormaPagamentoCadastroComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FormaPagamentoCadastroComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(FormaPagamentoCadastroComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
