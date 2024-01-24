import {Component, Input, OnInit} from '@angular/core';
import {MonitoraggioService} from "../monitoraggio.service";
import {Router} from "@angular/router";
import {Table} from "primeng/table";
import {AutenticazioneService} from "../../autenticazione/autenticazione.service";

@Component({
  selector: 'app-monitoraggio-operazioni-attive',
  templateUrl: './monitoraggio-operazioni-attive.component.html',
  styleUrls: ['./monitoraggio-operazioni-attive.component.scss']
})
export class MonitoraggioOperazioniAttiveComponent {

    operazioni: any[] = [];
    @Input() isAutotrasportatore:boolean=false;

    constructor(private router: Router,private service: MonitoraggioService,public autenticazioneService : AutenticazioneService) {}

    ngOnInit(){
        this.service.getAllOperazioni().subscribe(dati => {
            this.operazioni = dati;
            // Filtra le operazioni escludendo quelle con stato "Chiuso"
            this.operazioni = this.operazioni.filter(
                (operazione) => operazione.operazione.stato !== "Chiuso" && operazione.operazione.stato !== "Chiusa"
            );
            if(this.isAutotrasportatore){
                this.operazioni = this.operazioni.filter(
                    (operazione) => operazione.autotrasportatore.id === this.autenticazioneService.profile.profilo.id
                );
            }

            if(this.autenticazioneService?.profile?.operatore=='Operatore Mobile'){
                this.operazioni = this.operazioni.filter(
                    (operazione) => operazione.operatore_mobile && operazione.operatore_mobile.id && operazione.operazione.stato !== "Chiuso" && operazione.operazione.stato !== "Chiusa" && operazione.issue && operazione.issue.stato && operazione.issue.stato!='Chiuso' && operazione.issue.stato!='Chiusa' && operazione.operatore_mobile.id  === this.autenticazioneService.profile.profilo.id
                );
            }
        },error => {
            console.log(error);
        });
    }


    openDettagliOp(data: any) {
        if(this.autenticazioneService?.profile?.operatore=='Operatore Mobile'){
           data.noNuovaIssue=true;
           data.noChiamataAutorita = false;
           data.fromStorico = true;
        }
        else {
            data.noNuovaIssue = false;
            data.noChiamataAutorita = true;
        }
        this.router.navigate(['home/dettaglioOp'], {
            state: {
                dataJson: data
            }
        });

    }

    onGlobalFilter(dt1: Table, $event: Event) {

    }
}
