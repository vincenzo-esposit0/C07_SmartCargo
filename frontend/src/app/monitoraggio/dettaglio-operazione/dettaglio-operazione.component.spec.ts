import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DettaglioOperazioneComponent } from './dettaglio-operazione.component';

describe('DettaglioOperazioneComponent', () => {
    let component: DettaglioOperazioneComponent;
    let fixture: ComponentFixture<DettaglioOperazioneComponent>;

    beforeEach(async () => {
        await TestBed.configureTestingModule({
            declarations: [ DettaglioOperazioneComponent ]
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
