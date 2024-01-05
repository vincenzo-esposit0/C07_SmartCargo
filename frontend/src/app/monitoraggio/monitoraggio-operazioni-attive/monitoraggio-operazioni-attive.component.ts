import { Component, OnInit } from '@angular/core';
import {MonitoraggioService} from "../monitoraggio.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-monitoraggio-operazioni-attive',
  templateUrl: './monitoraggio-operazioni-attive.component.html',
  styleUrls: ['./monitoraggio-operazioni-attive.component.scss']
})
export class MonitoraggioOperazioniAttiveComponent {

    operazioni: any[] = [];

    constructor(private router: Router,private service: MonitoraggioService) {}

    ngOnInit(){

        this.service.getAllOperazioni().subscribe(dati => {
            this.operazioni = dati;
        },error => {
            console.log(error);
        });
    }


    openDettagliOp(operazione: any) {

        this.router.navigate(['home/dettaglioOp'], {
            state: {
                operazioneJson: operazione
            }
        });

    }
}
