import { Component, OnInit } from '@angular/core';
import {TestService} from "../../test.service";

@Component({
  selector: 'app-gestisci-issue',
  templateUrl: './gestisci-issue.component.html',
  styleUrls: ['./gestisci-issue.component.scss']
})
export class GestisciIssueComponent {
    showDialog: boolean = true;
    issue: any = {autotrasportatore: {}, issue: {}};
    tipiProblema: any[] = [{nome: "Anomalia Percorso"}, {nome: "Anomalia Carico/Scarico Merce"}];
    operatoriMob: any = [{id: 1, nome: "Paolo"},{id: 2, nome: "Amedeo"}];

    constructor(private service: TestService) {
    }

    ngOnInit(){
    }

    cancelTask() {

    }

    save() {
        this.service.inviaIssue(this.issue).subscribe(dati => {
            alert(JSON.stringify(dati));
        },dati => {
            return [];
        });
    }
}
