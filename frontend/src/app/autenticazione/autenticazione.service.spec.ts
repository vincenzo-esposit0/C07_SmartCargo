import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';

import { AutenticazioneService } from './autenticazione.service';

describe('AutenticazioneService', () => {
  let service: AutenticazioneService;

  beforeEach(() => {

    TestBed.configureTestingModule({
        imports: [HttpClientTestingModule],
        providers: [AutenticazioneService]
    });

    service = TestBed.inject(AutenticazioneService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
