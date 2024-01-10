import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MonitoraggioOperazioniCaricoScaricoComponent } from './monitoraggio-operazioni-carico-scarico.component';

describe('MonitoraggioOperazioniCaricoScaricoComponent', () => {
  let component: MonitoraggioOperazioniCaricoScaricoComponent;
  let fixture: ComponentFixture<MonitoraggioOperazioniCaricoScaricoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MonitoraggioOperazioniCaricoScaricoComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MonitoraggioOperazioniCaricoScaricoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
