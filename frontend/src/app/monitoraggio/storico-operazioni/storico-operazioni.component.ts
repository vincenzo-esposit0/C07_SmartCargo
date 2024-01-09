import { Component } from '@angular/core';
import {Router} from "@angular/router";
import {MonitoraggioService} from "../monitoraggio.service";

@Component({
  selector: 'app-storico-operazioni',
  templateUrl: './storico-operazioni.component.html',
  styleUrls: ['./storico-operazioni.component.scss']
})
export class StoricoOperazioniComponent {
    operazioni: any[] = [];
    filtro:any={autotrasportatore:'',azienda:'',dataDa:'',dataA:'',targa:''};
    filtroSelected:boolean=true;
    constructor(private router: Router,private service: MonitoraggioService) {}

    ngOnInit(){

    }


    cerca() {
        console.log(this.filtro);
        this.service.getStorico(this.filtro).subscribe(dati => {
            this.operazioni = dati;
            console.log(this.operazioni)
        },error => {
            console.log(error);
        });
    }
}
