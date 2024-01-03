import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegistraIngressoComponent } from './registra-ingresso.component';

describe('RegistraIngressoComponent', () => {
  let component: RegistraIngressoComponent;
  let fixture: ComponentFixture<RegistraIngressoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RegistraIngressoComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RegistraIngressoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
