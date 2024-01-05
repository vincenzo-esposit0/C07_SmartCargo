import { TestBed } from '@angular/core/testing';

import { MonitoraggioService } from './monitoraggio.service';

describe('MonitoraggioService', () => {
  let service: MonitoraggioService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MonitoraggioService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
