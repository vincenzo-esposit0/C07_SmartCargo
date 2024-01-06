import { Component } from '@angular/core';
import {IssueService} from "../../issue/issue.service";
import {DatePipe} from "@angular/common";
import {IngressoService} from "../ingresso.service";

@Component({
  selector: 'app-registra-ingresso',
  templateUrl: './registra-ingresso.component.html',
  styleUrls: ['./registra-ingresso.component.scss']
})
export class RegistraIngressoComponent {
    ingresso: any = {autotrasportatore: {},veicolo:{},merci:{},operazione:{},destinazione:'',operatoreIngresso_id:0};
    tipiProblema: any[] = [{nome: "Anomalia Percorso"}, {nome: "Anomalia Carico/Scarico Merce"}];
    tipiOp: any[] = [{nome: "Consegna"}, {nome: "Trasporto"},{nome:"Distribuzione"}];
    destinazioni: any[] = [{nome: "M1"}, {nome: "M2"}];
    operatoriMob: any = [{id: 1, nome: "Paolo"},{id: 2, nome: "Amedeo"}];
    selectedOpMobile: any = {};
    tipiMerce:any;
    tipiModello:any;
    constructor(private service: IngressoService, private datePipe: DatePipe) {}

    ngOnInit(){
        this.service.merci().subscribe(dati=> {
            this.tipiMerce=dati;
            console.log(dati);
        });
        this.service.modello().subscribe(dati=> {
            this.tipiModello=dati;
            console.log(dati);
        });
    }

    cancella() {
        this.ingresso = {};
        this.selectedOpMobile = {};
    }

    salvaIngresso() {
        this.ingresso.operatoreIngresso_id=1;
        this.service.registrazioneIngresso(this.ingresso).subscribe(dati => {
            console.log(dati);
        },error => {
            console.log(error);
        });
    }


    aggiornaTest() {

        /*
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

         */
    }
}
