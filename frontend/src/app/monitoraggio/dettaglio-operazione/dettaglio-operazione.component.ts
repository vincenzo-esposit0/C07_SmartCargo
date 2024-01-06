import { Component } from '@angular/core';
import {Router} from "@angular/router";

@Component({
  selector: 'app-dettaglio-operazione',
  templateUrl: './dettaglio-operazione.component.html',
  styleUrls: ['./dettaglio-operazione.component.scss']
})
export class DettaglioOperazioneComponent {

    data: any = {};
    options: any;

    content: any[] = [
        {icon: 'pi pi-fw pi-phone', title: 'Telefono', info:''},
        {icon: 'pi pi-fw pi-map-marker', title: 'Il nostro Ufficio', info: ''},
        {icon: 'pi pi-fw pi-print', title: 'Fax', info:+''}
    ];

    showDialog: boolean = false;

    //solo se nn ci sono già issue aperte sull'operazione
    showNewIssue : boolean = true;
    noIssue: boolean = false;

    constructor(private router: Router) {
        if (this.router.getCurrentNavigation()?.extras.state) {
            // @ts-ignore
            let routeState = this.router.getCurrentNavigation().extras.state;
            if (routeState) {
                // @ts-ignore
                this.data = routeState.dataJson;
            }
        }
    }


    ngOnInit(){

        let latitude = 40.85;
        let longitude = 14.4829;

        if(this.data){
            if(this.data.issue){
                if(this.data.issue?.stato == 'Aperta'){
                    this.showNewIssue = false;
                }
                else if(this.data.issue?.stato == 'Chiusa' || this.data.issue?.stato == 'Chiuso'){
                    this.noIssue = true;
                }
            }
            else this.data.issue = {};
        }


        this.options = {
            center: {lat: latitude, lng: longitude},
            zoom: 10,
        };
    }

    newIssue() {
        this.showDialog = true;
    }

    aggiornaIssue() {
        this.showDialog = true;
    }
}
