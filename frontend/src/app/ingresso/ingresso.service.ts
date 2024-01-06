import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import {HttpClient, HttpHeaders} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class IngressoService {

    constructor(private httpClient: HttpClient) { }


    merci(): Observable<any> {
        const merci = this.httpClient.get<any>('http://127.0.0.1:5000/merci');
        return merci;
    }

    modello(): Observable<any> {
        const modello = this.httpClient.get<any>('http://127.0.0.1:5000/modello');
        return modello;
    }

    registrazioneIngresso(data: any): Observable<any> {
        const headers = new HttpHeaders({
            'Content-Type': 'application/json'
        });
        return this.httpClient.post<any>('http://127.0.0.1:5000/registrazioneIngresso', JSON.stringify(data), { headers: headers });
    }

}
