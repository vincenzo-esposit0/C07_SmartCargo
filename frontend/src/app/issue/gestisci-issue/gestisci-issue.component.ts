import { Component, OnInit } from '@angular/core';
import {DatePipe} from "@angular/common";
import {IssueService} from "../issue.service";
import {UtenteService} from "../../utente/utente.service";

@Component({
  selector: 'app-gestisci-issue',
  templateUrl: './gestisci-issue.component.html',
  styleUrls: ['./gestisci-issue.component.scss']
})
export class GestisciIssueComponent {
    showDialog: boolean = true;
    issue: any = {autotrasportatore: {}};
    tipiProblema: any[] = [{nome: "Anomalia Percorso"}, {nome: "Anomalia Carico/Scarico Merce"}];
    operatoriMob: any = [{id: 1, nome: "Paolo"},{id: 2, nome: "Amedeo"}];
    selectedOpMobile: any = {};

    constructor(private service: IssueService, private datePipe: DatePipe, private utenteService : UtenteService) {}

    ngOnInit(){

        this.utenteService.getAutotrasportatoreById("3").subscribe(dati => {
           console.log(dati);
           this.issue.autotrasportatore.nome = dati.nome;
           this.issue.autotrasportatore.cognome = dati.cognome;
           this.issue.autotrasportatore.azienda = dati.azienda;
           this.issue.autotrasportatore.targa = dati?.targa;
        },error => {
            console.log(error);
        });
    }

    cancella() {
        this.issue = {};
        this.selectedOpMobile = {};
        this.showDialog = false;
    }

    salvaNuovaIssue() {

        //dati fake to-do
        this.issue.stato = "Aperta";
        this.issue.operatoreSala_id = 1; //id dell'utente corrente
        this.issue.operatoreMobile_id = this.selectedOpMobile.id; //da chiedere lato server la lista di tutti gli operatori
        this.issue.operazione_id = 3;//operazione su cui hai cliccato da passare come parametro al componente gestisci issue
        this.issue.timestampChiusura = "";
        this.issue.timestampApertura = this.datePipe.transform(this.issue.timestampApertura, 'yyyy-MM-ddTHH:mm:ss');
        this.issue.tipologiaProblema = this.issue.tipologiaProblema.nome;
        this.service.inviaIssue(this.issue).subscribe(dati => {
           console.log(dati);
        },error => {
            console.log(error);
        });
    }


    aggiornaTest() {
        this.issue.id = 3
        this.issue.stato = "Chiusa";
        this.issue.operatoreSala_id = 1; //id dell'utente corrente
        this.issue.operatoreMobile_id = this.selectedOpMobile.id; //da chiedere lato server la lista di tutti gli operatori
        this.issue.operazione_id = 3;//operazione su cui hai cliccato da passare come parametro al componente gestisci issue
        this.issue.timestampChiusura = "";
        this.issue.timestampApertura = this.datePipe.transform(this.issue.timestampApertura, 'yyyy-MM-ddTHH:mm:ss');
        this.issue.tipologiaProblema = this.issue.tipologiaProblema.nome;
        this.service.aggiornaIssue(this.issue).subscribe(dati => {
            console.log(dati);
        },error => {
            console.log(error);
        });
    }
}
