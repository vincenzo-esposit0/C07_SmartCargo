import { TestBed } from '@angular/core/testing';

import { UtenteService } from './utente.service';
import {HttpClientTestingModule} from "@angular/common/http/testing";
import {AutenticazioneService} from "../autenticazione/autenticazione.service";

describe('UtenteService', () => {
  let service: UtenteService;

  beforeEach(() => {
    TestBed.configureTestingModule({
        imports: [HttpClientTestingModule],
        providers: [UtenteService]
    });
    service = TestBed.inject(UtenteService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
