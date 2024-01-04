import { Component } from '@angular/core';
import {Router} from "@angular/router";
import {AutenticazioneService} from "../autenticazione.service";

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.scss']
})
export class SignUpComponent {

    constructor(private router: Router,private autenticazioneService : AutenticazioneService){}
    autotrasportatore: any = {};

    cancella() {

    }

    inserisci() {

    }
}
