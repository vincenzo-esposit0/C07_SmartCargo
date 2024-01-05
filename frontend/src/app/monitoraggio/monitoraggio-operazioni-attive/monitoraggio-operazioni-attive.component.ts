import { Component, OnInit } from '@angular/core';
import {MonitoraggioService} from "../monitoraggio.service";
import {Router} from "@angular/router";
import {Table} from "primeng/table";

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


    openDettagliOp(data: any) {

        this.router.navigate(['home/dettaglioOp'], {
            state: {
                dataJson: data
            }
        });

    }

    onGlobalFilter(dt1: Table, $event: Event) {

    }
}
