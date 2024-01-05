import { Component } from '@angular/core';
import {Router} from "@angular/router";

@Component({
  selector: 'app-dettaglio-operazione',
  templateUrl: './dettaglio-operazione.component.html',
  styleUrls: ['./dettaglio-operazione.component.scss']
})
export class DettaglioOperazioneComponent {

    operazione: any = {};
    options: any;

    content: any[] = [
        {icon: 'pi pi-fw pi-phone', title: 'Telefono', info:''},
        {icon: 'pi pi-fw pi-map-marker', title: 'Il nostro Ufficio', info: ''},
        {icon: 'pi pi-fw pi-print', title: 'Fax', info:+''}
    ];
    showNewIssueComponent: boolean = false;
    showModificaIssueComponent: boolean = false;

    constructor(private router: Router) {
        if (this.router.getCurrentNavigation()?.extras.state) {
            // @ts-ignore
            let routeState = this.router.getCurrentNavigation().extras.state;
            if (routeState) {
                // @ts-ignore
                this.operazione = routeState.operazioneJson;
            }
        }
    }

    ngOnInit(){

        let latitude = 40.85;
        let longitude = 14.4829;

        this.options = {
            center: {lat: latitude, lng: longitude},
            zoom: 10,
        };
    }

    newIssue() {
        this.showNewIssueComponent = true;

    }

    aggiornaIssue() {
        this.showModificaIssueComponent = true;
    }
}
