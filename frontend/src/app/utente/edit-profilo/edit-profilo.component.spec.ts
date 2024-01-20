import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditProfiloComponent } from './edit-profilo.component';
import {HttpClientTestingModule} from "@angular/common/http/testing";
import {AutenticazioneService} from "../../autenticazione/autenticazione.service";
import {UtenteService} from "../utente.service";

describe('EditProfiloComponent', () => {
  let component: EditProfiloComponent;
  let fixture: ComponentFixture<EditProfiloComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EditProfiloComponent ],
        imports: [HttpClientTestingModule],
        providers: [UtenteService]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EditProfiloComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
