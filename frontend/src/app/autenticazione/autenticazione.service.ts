import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class AutenticazioneService {
    profile: any=null;

    constructor(private httpClient: HttpClient) { }
    login(data: any): Observable<any> {
        const headers = new HttpHeaders({
            'Content-Type': 'application/json'
        });
        return this.httpClient.post<any>('http://127.0.0.1:5000/login', JSON.stringify(data), { headers: headers });
    }

    registrazione(data: any): Observable<any> {
        const headers = new HttpHeaders({
            'Content-Type': 'application/json'
        });
        return this.httpClient.post<any>('http://127.0.0.1:5000/registrazione', JSON.stringify(data), { headers: headers });
    }

    modifica(data: any): Observable<any> {
        const headers = new HttpHeaders({
            'Content-Type': 'application/json'
        });
        return this.httpClient.post<any>('http://127.0.0.1:5000/modificaOperatore', JSON.stringify(data), { headers: headers });
    }

}
