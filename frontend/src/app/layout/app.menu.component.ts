import { OnInit } from '@angular/core';
import { Component } from '@angular/core';

@Component({
    selector: 'app-menu',
    templateUrl: './app.menu.component.html'
})
export class AppMenuComponent implements OnInit {

    model: any[] = [];

    ngOnInit() {
        this.model=[ {
            label: 'Utente',
            icon: 'pi pi-home',
            items: [
                {
                    label: 'Registrazione ingresso',
                    icon: 'pi pi-fw pi-image',
                    routerLink: ['ingresso']
                },
                {
                    label: 'Monitoraggio Operazioni Attive',
                    icon: 'pi pi-fw pi-image',
                    routerLink: ['monitoraggioOpAttive']
                }
            ]
        }]

    }
}
