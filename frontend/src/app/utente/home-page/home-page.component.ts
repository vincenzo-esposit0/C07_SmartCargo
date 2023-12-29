import { Component } from '@angular/core';
import {TestService} from "../../test.service";

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss']
})
export class HomePageComponent {

    constructor(private service: TestService) {}

    objList: any[] = [];
    value: number = 1;


    getObjList() : any{

        this.service.getObjList().subscribe(dati => {
            alert(JSON.stringify(dati));
            return dati;
        },dati => {
            return [];
        });
    }


    getObj(id: number): any{
        alert("id: "+id);
        this.service.getObj(id.toString()).subscribe(dati => {
            alert(JSON.stringify(dati));
            return dati;
        },dati => {
            return {};
        });
    }
}
