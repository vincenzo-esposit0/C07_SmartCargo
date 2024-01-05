import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class MonitoraggioService {

    constructor(private httpClient: HttpClient) { }


    getAllOperazioni(): Observable<any>{
        const issues = this.httpClient.get<any>('http://127.0.0.1:5000/operazioni/getAll');
        return issues;
    }
}
