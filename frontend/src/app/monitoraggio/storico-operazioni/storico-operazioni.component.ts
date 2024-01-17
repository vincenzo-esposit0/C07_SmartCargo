import {Component, ViewChild} from '@angular/core';
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

    @ViewChild('dt1', { static: false }) dt1: any;

    ngOnInit(){
        this.cerca();
    }


    cerca() {
        this.service.getStorico(this.filtro).subscribe(dati => {
            this.operazioni = dati;
            console.log(this.operazioni)
            console.log(dati);
        },error => {
            console.log(error);
        });
    }

    applyFilterGlobal($event: Event) {
        this.dt1.filterGlobal(($event.target as HTMLInputElement).value, 'contains');
    }

    openDettagliOp(data: any) {
        data.fromStorico = true;
        this.router.navigate(['home/dettaglioOp'], {
            state: {
                dataJson: data
            }
        });
    }
}
