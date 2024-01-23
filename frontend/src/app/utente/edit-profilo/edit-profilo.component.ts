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
                    this.profilo.tipo = 'Autotrasportatore';
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
        if(this.checkFormValidity()) {
            this.autenticazioneService.modifica(this.profilo).subscribe(dati => {
                let value = dati;
            }, error => {
            });
        }
    }

    checkFormValidity(): boolean {
        const emailRegex = /^[A-z0-9._%+-]+@[A-z0-9.-]+\.[A-z]{2,10}$/;
        const passwordRegex = /^.{8,}$/;
        const indirizzoRegex = /^([a-zA-Zà-úÀ-Ú0-9\s.'-]+),\s*(\d+),\s*([a-zA-Zà-úÀ-Ú\s.'-]+),\s*([0-9]{5})$/;


        if (!indirizzoRegex.test(this.profilo.indirizzo)) {
            this.messageService.add({ severity: 'error', summary: 'Errore', detail: 'Indirizzo non valido' });
            return false;

        }


        if (!emailRegex.test(this.profilo.email)) {
            this.messageService.add({ severity: 'error', summary: 'Errore', detail: 'Email non valida' });
            return false;
        }
        if (!passwordRegex.test(this.profilo.password)) {
            this.messageService.add({ severity: 'error', summary: 'Errore', detail: 'Password non valida' });
            return false;
        }
        return true;
    }

}
