import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GestisciIssueComponent } from './gestisci-issue.component';

describe('GestisciIssueComponent', () => {
    let component: GestisciIssueComponent;
    let fixture: ComponentFixture<GestisciIssueComponent>;

    beforeEach(async () => {
        await TestBed.configureTestingModule({
            declarations: [ GestisciIssueComponent ]
        })
            .compileComponents();

        fixture = TestBed.createComponent(GestisciIssueComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });
});
