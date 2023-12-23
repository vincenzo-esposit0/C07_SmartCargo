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
                    label: 'Edit Profilo',
                    icon: 'pi pi-fw pi-image',
                    routerLink: ['/dashboard-banking']
                }
            ]
        }]

    }
}
