import { Component } from '@angular/core';
import {Router} from "@angular/router";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})

export class LoginComponent {

    username: any='';
    password: any='';
    constructor(private router: Router){}

    login($event: MouseEvent) {
        if(this.username){
            if(this.password){
                this.router.navigate(['home']);
            }
        }
    }
}
