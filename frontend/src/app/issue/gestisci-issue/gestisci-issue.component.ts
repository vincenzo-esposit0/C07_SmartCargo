import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {DatePipe} from "@angular/common";
import {IssueService} from "../issue.service";
import {UtenteService} from "../../utente/utente.service";
import {MessageService} from "primeng/api";
import {AutenticazioneService} from "../../autenticazione/autenticazione.service";

@Component({
  selector: 'app-gestisci-issue',
  templateUrl: './gestisci-issue.component.html',
  styleUrls: ['./gestisci-issue.component.scss'],
    providers:[MessageService]
})
export class GestisciIssueComponent {
    showDialog: boolean = true;
    issue: any = {};
    tipiProblema: any[] = [{nome: "Anomalia Percorso"}, {nome: "Anomalia Carico/Scarico Merce"}];
    operatoriMob: any = [{id: 1, nome: "Paolo"},{id: 2, nome: "Amedeo"}];
    selectedOpMobile: any = {};

    @Input() data: any = {};
    modalitaEdit: boolean = false; //significa che già esiste un issue

    @Output() disableDialog = new EventEmitter<any>();

    constructor(private auth: AutenticazioneService,private messageService: MessageService,private service: IssueService, private datePipe: DatePipe, private utenteService : UtenteService) {}

    ngOnInit(){
        console.log(this.data);

        if(this.data){
            if(this.data.issue){
                if(this.data.issue?.stato == 'Aperta' || this.data.issue?.stato == 'Aperto')
                    this.modalitaEdit = true;
                else if(this.data.issue.id === undefined || this.data.issue.id == null){
                    this.data.issue = {};
                    this.data.issue.timestampApertura = new Date();
                    this.data.issue.posizione = "37.7749, -122.4194";
                    this.data.issue.descrizione = ""
                }
            }
        }

    }

    cancella() {
        this.issue = {};
        this.selectedOpMobile = {};
        this.showDialog = false;
    }

    salvaNuovaIssue() {

        if(!this.checkFormValidity()) return;

        this.data.issue.stato = "Aperta";
        this.data.issue.operatoreSala_id = this.auth.profile.profilo.id;
        this.data.issue.operazione_id = this.data.operazione.id;
        this.data.issue.timestampApertura = this.datePipe.transform(this.data.issue.timestampApertura, 'yyyy-MM-ddTHH:mm:ss');
        this.data.issue.timestampChiusura = this.datePipe.transform(this.data.issue.timestampApertura, 'yyyy-MM-ddTHH:mm:ss');

        this.data.issue.operatoreMobile_id = this.selectedOpMobile.id;

        this.data.issue.tipologiaProblema = this.data.issue.tipologiaProblema.nome
        this.service.inviaIssue(this.data.issue).subscribe(dati => {
            this.disableDialog.emit(false);
            this.showDialog = false;
        },error => {
            this.showDialog = false;
            this.disableDialog.emit(false);
            console.log(error);
        });
    }


    aggiorna() {

        if(!this.checkFormValidity()) return;

        this.data.issue.timestampApertura = this.datePipe.transform(this.data.issue.timestampApertura, 'yyyy-MM-ddTHH:mm:ss');
        this.data.issue.timestampChiusura = this.datePipe.transform(this.data.issue.timestampApertura, 'yyyy-MM-ddTHH:mm:ss');


        this.data.issue.operatoreMobile_id = this.selectedOpMobile.id;
        this.data.issue.tipologiaProblema = this.data.issue.tipologiaProblema.nome
        this.service.aggiornaIssue(this.data.issue).subscribe(dati => {
            this.showDialog = false;
            this.disableDialog.emit(false);
        },error => {
            this.showDialog = false;
            console.log(error);
            this.disableDialog.emit(false);
        });
    }



    checkFormValidity(): boolean {
        const posizoneRegex = /^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?)\s*[,]\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$/;

        const input = this.data.issue.posizione;

        if (!posizoneRegex.test(input)) {
            this.messageService.add({ severity: 'error', summary: 'Errore', detail: 'Coordinate Posizione non valide' });
            return false;
        }

        const maxLength250Regex = /^.{1,254}$/;

        if (!maxLength250Regex.test(this.data.issue.descrizione) || this.data.issue.descrizione.trim().length <= 0) {
            this.messageService.add({ severity: 'error', summary: 'Errore', detail: 'Descrizione non valida!' });
            return false;
        }


        return true;

    }





}
