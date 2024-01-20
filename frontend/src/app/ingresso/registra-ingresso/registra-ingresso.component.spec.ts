import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { RegistraIngressoComponent } from './registra-ingresso.component';
import {IngressoService} from "../ingresso.service";

describe('RegistraIngressoComponent', () => {
  let component: RegistraIngressoComponent;
  let fixture: ComponentFixture<RegistraIngressoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RegistraIngressoComponent ],
        imports: [HttpClientTestingModule],
        providers: [IngressoService]
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
