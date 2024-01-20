import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StoricoOperazioniComponent } from './storico-operazioni.component';
import {HttpClientTestingModule} from "@angular/common/http/testing";
import {UtenteService} from "../../utente/utente.service";
import {MonitoraggioService} from "../monitoraggio.service";

describe('StoricoOperazioniComponent', () => {
  let component: StoricoOperazioniComponent;
  let fixture: ComponentFixture<StoricoOperazioniComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StoricoOperazioniComponent ],
        imports: [HttpClientTestingModule],
        providers: [MonitoraggioService]
    })
    .compileComponents();

    fixture = TestBed.createComponent(StoricoOperazioniComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
