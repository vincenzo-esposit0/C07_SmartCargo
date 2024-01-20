import { TestBed } from '@angular/core/testing';

import { MonitoraggioService } from './monitoraggio.service';
import {HttpClientTestingModule} from "@angular/common/http/testing";
import {AutenticazioneService} from "../autenticazione/autenticazione.service";

describe('MonitoraggioService', () => {
  let service: MonitoraggioService;

  beforeEach(() => {
    TestBed.configureTestingModule({
        imports: [HttpClientTestingModule],
        providers: [MonitoraggioService]
    });
    service = TestBed.inject(MonitoraggioService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
