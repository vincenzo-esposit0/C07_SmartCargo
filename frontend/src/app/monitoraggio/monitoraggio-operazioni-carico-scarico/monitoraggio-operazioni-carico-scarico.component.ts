import { Component } from '@angular/core';
import {Table} from "primeng/table";
import {Router} from "@angular/router";
import {MonitoraggioService} from "../monitoraggio.service";
import {ConfirmationService, MessageService} from "primeng/api";
import {AutenticazioneService} from "../../autenticazione/autenticazione.service";

@Component({
  selector: 'app-monitoraggio-operazioni-carico-scarico',
  templateUrl: './monitoraggio-operazioni-carico-scarico.component.html',
  styleUrls: ['./monitoraggio-operazioni-carico-scarico.component.scss'],
    providers: [ConfirmationService,MessageService]
})
export class MonitoraggioOperazioniCaricoScaricoComponent {

    operazioni: any[] = [];
    selectedOperazione: any = {};
    showSegnalaEsitoDialog: boolean = false;

    constructor(private auth: AutenticazioneService,private router: Router,private service: MonitoraggioService, private confirm: ConfirmationService, private message: MessageService) {}

    ngOnInit(){

        this.service.getOpCarScar(this.auth.profile.profilo).subscribe(dati => {
            this.operazioni = dati;
            if(this.operazioni.length > 0){
                this.operazioni = this.operazioni.filter(
                    (operazione) => operazione.operazione.stato !== "Terminata"
                );
            }

        },error => {
            console.log(error);
        });
    }


    openDettagliOp(data: any) {

        this.router.navigate(['home/dettaglioOp'], {
            state: {
                dataJson: data
            }
        });

    }

    segnalaEsito(esito: boolean) {
        //esito positivo
        if(esito){
            this.selectedOperazione.stato = "Chiuso";
            this.service.segnalaEsito(this.selectedOperazione).subscribe(dati => {

                this.selectedOperazione = {};
            },error => {
                console.log(error);
                this.selectedOperazione = {};
            });

        }
        //esito negativo
        else {
            this.selectedOperazione.stato = "Anomalia Carico/Scarico";
            this.service.segnalaEsito(this.selectedOperazione).subscribe(dati => {
                this.selectedOperazione = {};
            },error => {
                console.log(error);
                this.selectedOperazione = {};
            });
        }

        this.showSegnalaEsitoDialog = false;

    }
}
