import { Component } from '@angular/core';
import {Router} from "@angular/router";
import {AutenticazioneService} from "../autenticazione.service";
import {MessageService} from "primeng/api";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
  providers:[MessageService]
})

export class LoginComponent {

    username: any='';
    password: any='';
    showAuth: boolean = false;
    codice: string = "";
    constructor(private messageService: MessageService,private router: Router,private autenticazioneService : AutenticazioneService){}

    login($event: MouseEvent) {
        if(this.username){
            if(this.password){
                if(!this.autenticazioneService.profile){
                    this.autenticazioneService.profile={};
                    let profilo={username:"",password:""};
                    profilo.username=this.username;
                    profilo.password=this.password
                    this.autenticazioneService.login(profilo).subscribe(dati => {
                        let value=dati;
                        if(value.stato==200){
                            this.autenticazioneService.profile.username=this.username;
                            this.autenticazioneService.profile.password=this.password;
                            this.router.navigate(['home']);
                        }else{
                            this.messageService.add({ severity: 'error', summary: 'Login', detail: value.message });
                        }
                    },error => {
                        console.log(error);
                    });

                }

            }
        }
    }

    checkCodice() {
        if(this.codice == "123456")  this.router.navigate(['registrati']);
        else this.messageService.add({ severity: 'error', summary: 'Autenticazione', detail: 'Codice Errato!' });

    }
}
