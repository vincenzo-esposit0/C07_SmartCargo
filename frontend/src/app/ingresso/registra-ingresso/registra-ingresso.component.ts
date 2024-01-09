import { Component } from '@angular/core';
import {IssueService} from "../../issue/issue.service";
import {DatePipe} from "@angular/common";
import {IngressoService} from "../ingresso.service";
import {MessageService} from "primeng/api";

@Component({
  selector: 'app-registra-ingresso',
  templateUrl: './registra-ingresso.component.html',
  styleUrls: ['./registra-ingresso.component.scss'],
    providers:[MessageService]
})
export class RegistraIngressoComponent {
    ingresso: any = {autotrasportatore: {},veicolo:{},merci:{},operazione:{},destinazione:'',operatoreIngresso_id:0};
    tipiProblema: any[] = [{nome: "Anomalia Percorso"}, {nome: "Anomalia Carico/Scarico Merce"}];
    tipiOp: any[] = [{nome: "Consegna"}, {nome: "Trasporto"},{nome:"Distribuzione"}];
    destinazioni: any[] = [{nome: "M1"}, {nome: "M2"}, {nome: "M3"}];
    operatoriMob: any = [{id: 1, nome: "Paolo"},{id: 2, nome: "Amedeo"}];
    selectedOpMobile: any = {};
    tipiMerce:any;
    tipiModello:any;
    visibile:boolean=true;
    visibileQr:boolean=false;
    qrCode:any;
    constructor(private messageService: MessageService,private service: IngressoService, private datePipe: DatePipe) {}

    ngOnInit(){
        this.ingresso.operazione.descrizione = "";
        this.ingresso.autotrasportatore.nome = this.ingresso.autotrasportatore.cognome = this.ingresso.autotrasportatore.azienda = "";
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

        if(!this.checkFormValidity()) return;

        this.ingresso.operatoreIngresso_id=1;
        this.service.registrazioneIngresso(this.ingresso).subscribe(dati => {
            console.log(dati);
        },error => {
            console.log(error);
        });
    }

    checkFormValidity(): boolean {

        const nomeRegex = /^[a-zA-Z\s.'-]{2,30}$/;
        const cognomeRegex = /^[a-zA-Z\s.'-]{2,30}$/;
        const aziendaRegex = /^[a-zA-Z0-9\s.'-]{3,30}$/;

        if (!nomeRegex.test(this.ingresso.autotrasportatore.nome) || this.ingresso.autotrasportatore.nome.trim().length <= 0) {
            this.messageService.add({ severity: 'error', summary: 'Errore', detail: 'Nome non valido' });
            return false;
        }

        if (!cognomeRegex.test(this.ingresso.autotrasportatore.cognome) || this.ingresso.autotrasportatore.cognome.trim().length <= 0) {
            this.messageService.add({ severity: 'error', summary: 'Errore', detail: 'Cognome non valido' });
            return false;

        }
        if (!aziendaRegex.test(this.ingresso.autotrasportatore.azienda) || this.ingresso.autotrasportatore.azienda.trim().length <= 0) {
            this.messageService.add({ severity: 'error', summary: 'Errore', detail: 'Azienda non valida' });
            return false;

        }

        const qtaRegex = /^[1-9]\d*$/;

        if (!qtaRegex.test(this.ingresso.merci.quantita)) {
            this.messageService.add({ severity: 'error', summary: 'Errore', detail: 'Quantità non valida' });
            return false;
        }

        const maxLength250Regex = /^.{1,254}$/;

        if (!maxLength250Regex.test(this.ingresso.operazione.descrizione) || this.ingresso.operazione.descrizione.trim().length <= 0) {
            this.messageService.add({ severity: 'error', summary: 'Errore', detail: 'Descrizione non valida!' });
            return false;
        }

        return true;

    }

    cerca() {
        let dati={qrCode_id:1}
        this.service.qrCodeIngresso(dati).subscribe(dati=> {
            console.log(dati);
        });
    }

    confermaCodice() {
        this.visibileQr=true;

    }
}
