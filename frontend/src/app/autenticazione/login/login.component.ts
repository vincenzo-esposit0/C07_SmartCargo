import { Component } from '@angular/core';
import {Router} from "@angular/router";
import {AutenticazioneService} from "../autenticazione.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})

export class LoginComponent {

    username: any='';
    password: any='';
    constructor(private router: Router,private autenticazioneService : AutenticazioneService){}

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
                            console.log(value.message);
                        }
                        console.log(dati);
                    },error => {
                        console.log(error);
                    });
                    console.log(JSON.stringify(this.autenticazioneService.profile));

                }

            }
        }
    }
}
