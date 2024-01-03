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
                    label: 'Gestisci Issue test',
                    icon: 'pi pi-fw pi-image',
                    routerLink: ['issue']
                },
                {
                    label: 'Registrazione ingresso',
                    icon: 'pi pi-fw pi-image',
                    routerLink: ['ingresso']
                }
            ]
        }]

    }
}
