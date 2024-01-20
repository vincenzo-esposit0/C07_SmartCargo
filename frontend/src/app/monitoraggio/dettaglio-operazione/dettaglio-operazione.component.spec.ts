import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DettaglioOperazioneComponent } from './dettaglio-operazione.component';
import {HttpClientTestingModule} from "@angular/common/http/testing";
import {MonitoraggioService} from "../monitoraggio.service";

describe('DettaglioOperazioneComponent', () => {
  let component: DettaglioOperazioneComponent;
  let fixture: ComponentFixture<DettaglioOperazioneComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DettaglioOperazioneComponent ],
        imports: [HttpClientTestingModule],
        providers: [MonitoraggioService]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DettaglioOperazioneComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
