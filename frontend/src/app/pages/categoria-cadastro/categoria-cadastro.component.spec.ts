import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CategoriaCadastroComponent } from './categoria-cadastro.component';

describe('CategoriaCadastroComponent', () => {
  let component: CategoriaCadastroComponent;
  let fixture: ComponentFixture<CategoriaCadastroComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CategoriaCadastroComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CategoriaCadastroComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
