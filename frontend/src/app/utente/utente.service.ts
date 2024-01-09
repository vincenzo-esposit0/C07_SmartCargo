import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class UtenteService {

    constructor(private httpClient: HttpClient) { }

    login(data: any): Observable<any> {
        const headers = new HttpHeaders({
            'Content-Type': 'application/json'
        });
        return this.httpClient.post<any>('http://127.0.0.1:5000/login', JSON.stringify(data), { headers: headers });
    }

    getAutotrasportatoreById(id: string): Observable<any>{
        const obj = this.httpClient.get<any>('http://127.0.0.1:5000/autotrasportatore/getById/'+id);
        return obj;
    }
}
