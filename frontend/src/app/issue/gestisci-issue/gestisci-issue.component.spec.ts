import { ComponentFixture, TestBed } from '@angular/core/testing';
import {HttpClientTestingModule} from "@angular/common/http/testing";
import { GestisciIssueComponent } from './gestisci-issue.component';
import {IssueService} from "../issue.service";

describe('GestisciIssueComponent', () => {
  let component: GestisciIssueComponent;
  let fixture: ComponentFixture<GestisciIssueComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GestisciIssueComponent ],
        imports: [HttpClientTestingModule],
        providers: [IssueService]
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
