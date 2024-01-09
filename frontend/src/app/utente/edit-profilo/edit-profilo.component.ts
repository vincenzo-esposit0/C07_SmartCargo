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
    constructor(private messageService: MessageService,private router: Router,private autenticazioneService : AutenticazioneService){}
    profilo:any;
    ngOnInit() {
        this.profilo=this.autenticazioneService.profile.profilo;

      console.log(this.autenticazioneService.profile.profilo);
    }


}
