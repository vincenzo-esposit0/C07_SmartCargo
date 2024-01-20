import { Component } from '@angular/core';
import {Router} from "@angular/router";
import {AutenticazioneService} from "./autenticazione/autenticazione.service";
import {Title} from "@angular/platform-browser";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'frontend';

  constructor(private autenticazioneService : AutenticazioneService,private router : Router,private titleService: Title){}

  ngOnInit() {
      this.titleService.setTitle('SmartCargo');
      if(!this.autenticazioneService.profile)
          this.router.navigate(['login']);
  }


}
