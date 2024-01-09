import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import {HttpClient, HttpHeaders} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class MonitoraggioService {

    constructor(private httpClient: HttpClient) { }


    getAllOperazioni(): Observable<any>{
        const issues = this.httpClient.get<any>('http://127.0.0.1:5000/operazioni/getAll');
        return issues;
    }

    getStorico(data: any): Observable<any>{
            const headers = new HttpHeaders({
                'Content-Type': 'application/json'
            });
            return this.httpClient.post<any>('http://127.0.0.1:5000/getStorico', JSON.stringify(data), { headers: headers });
    }
}
