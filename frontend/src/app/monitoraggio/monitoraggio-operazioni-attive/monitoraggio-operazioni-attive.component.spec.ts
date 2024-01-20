import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MonitoraggioOperazioniAttiveComponent } from './monitoraggio-operazioni-attive.component';
import {HttpClientTestingModule} from "@angular/common/http/testing";
import {MonitoraggioService} from "../monitoraggio.service";

describe('MonitoraggioOperazioniAttiveComponent', () => {
  let component: MonitoraggioOperazioniAttiveComponent;
  let fixture: ComponentFixture<MonitoraggioOperazioniAttiveComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MonitoraggioOperazioniAttiveComponent ],
        imports: [HttpClientTestingModule],
        providers: [MonitoraggioService]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MonitoraggioOperazioniAttiveComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
