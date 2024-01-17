import { Component } from '@angular/core';
import {MessageService} from "primeng/api";
import {Router} from "@angular/router";
import {AutenticazioneService} from "../../autenticazione/autenticazione.service";
@Component({
  selector: 'app-edit-profilo',
  templateUrl: './edit-profilo.component.html',
  styleUrls: ['./edit-profilo.component.scss']
})
export class EditProfiloComponent {
    constructor(private messageService: MessageService,private router: Router,public autenticazioneService : AutenticazioneService){}
    profilo:any;
    qrCode:any;
    visibile:boolean=true;
    visibileQr:boolean=false;
    ngOnInit() {
        this.profilo=this.autenticazioneService.profile.profilo;
        this.profilo.id=this.autenticazioneService.profile.profilo.id;
        this.profilo.dataNascita='1989-06-21';
        this.qrCode='AUTOTRASPORTATORE'+'_'+this.profilo.id;
        if(this.autenticazioneService.profile.operatore==='Operatore Sala'){

                this.profilo.tipo='OpSala';
            }else {
                if (this.autenticazioneService.profile.operatore == 'Autotrasportatore') {
                } else {
                    if (this.autenticazioneService.profile.operatore === 'Operatore Magazzino') {
                        this.profilo.tipo = 'OpMagazzino';
                    } else {
                        if (this.autenticazioneService.profile.operatore === 'Operatore Mobile') {
                            this.profilo.tipo = 'OpMobile';

                        }
                    }
                }
            }

}


    modifica() {
        console.log(JSON.stringify(this.profilo));
        this.autenticazioneService.modifica(this.profilo).subscribe(dati => {
            let value = dati;
        }, error => {
            console.log(error);
        });

    }
}
