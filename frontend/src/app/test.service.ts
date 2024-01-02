import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import {HttpClient, HttpHeaders} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class TestService {

    constructor(private httpClient: HttpClient) { }

    getObjList(): Observable<any>{
        const objList = this.httpClient.get<any>('http://127.0.0.1:5000/list');
        return objList;
    }

    getObj(id: string): Observable<any>{
        const obj = this.httpClient.get<any>('http://127.0.0.1:5000/detail/'+id);
        return obj;
    }

    inviaIssue(data: any): Observable<any> {
        // Imposta le intestazioni per indicare che stai inviando JSON
        const headers = new HttpHeaders({
            'Content-Type': 'application/json'
        });

        // Effettua la richiesta POST al tuo server Flask
        return this.httpClient.post<any>('http://127.0.0.1:5000/issue/newIssue', data, { headers: headers });
    }

}

