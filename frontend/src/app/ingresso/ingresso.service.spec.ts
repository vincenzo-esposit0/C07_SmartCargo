import { TestBed } from '@angular/core/testing';

import { IngressoService } from './ingresso.service';
import {HttpClientTestingModule} from "@angular/common/http/testing";
import {AutenticazioneService} from "../autenticazione/autenticazione.service";

describe('IngressoService', () => {
  let service: IngressoService;

  beforeEach(() => {
    TestBed.configureTestingModule({
        imports: [HttpClientTestingModule],
        providers: [AutenticazioneService]
    });
    service = TestBed.inject(IngressoService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
