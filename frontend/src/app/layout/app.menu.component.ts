import { OnInit } from '@angular/core';
import { Component } from '@angular/core';
import {AutenticazioneService} from "../autenticazione/autenticazione.service";
import {Router} from "@angular/router";

@Component({
    selector: 'app-menu',
    templateUrl: './app.menu.component.html'
})
export class AppMenuComponent implements OnInit {

    model: any[] = [];
    constructor(private autenticazioneService : AutenticazioneService){}

    ngOnInit() {
        let registrazioneIngresso=  {
            label: 'Registrazione ingresso',
            icon: 'pi pi-fw pi-file',
            routerLink: ['ingresso']
        };

        let monitoraggio=
        {
            label: 'Monitoraggio Operazioni Attive',
            icon: 'pi pi-fw pi-desktop',
            routerLink: ['monitoraggioOpAttive']
        };

        let monitaggioCaricoScarico=
        {
            label: 'Monitoraggio Operazioni Carico Scarico',
            icon: 'pi pi-fw pi-truck',
            routerLink: ['monitoraggioOpCarScar']
        };

        let storico=
            {
                label: 'Storico',
                icon: 'pi pi-fw pi-history',
                routerLink: ['storico']
            };

        let home=
            {
                label: 'Home',
                icon: 'pi pi-fw pi-home',
                routerLink: ['dashboard']
            };

        this.model=[];

        if(this.autenticazioneService.profile){
            this.model.push(home);
            if(this.autenticazioneService.profile.operatore==='Autotrasportatore'){
            }else{
                if(this.autenticazioneService.profile.operatore==='Operatore Ingresso'){
                    this.model.push(registrazioneIngresso);
                }else{
                    if(this.autenticazioneService.profile.operatore==='Operatore Sala'){
                        this.model.push(monitoraggio);
                        this.model.push(storico);
                    }else{
                        if(this.autenticazioneService.profile.operatore==='Operatore Magazzino'){
                            this.model.push(monitaggioCaricoScarico);
                        }else{
                            // TODO inserire operatore mobile
                        }
                    }
                }
            }

        }
    }
}
