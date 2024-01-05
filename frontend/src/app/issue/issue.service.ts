import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import {HttpClient, HttpHeaders} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class IssueService {

    constructor(private httpClient: HttpClient) { }


    inviaIssue(data: any): Observable<any> {
        const headers = new HttpHeaders({
            'Content-Type': 'application/json'
        });

        return this.httpClient.post<any>('http://127.0.0.1:5000/issue/newIssue', JSON.stringify(data), { headers: headers });
    }

    getAllIssue(): Observable<any>{
        const issues = this.httpClient.get<any>('http://127.0.0.1:5000/issue/getAll');
        return issues;
    }

    getIssueById(id: string): Observable<any>{
        const obj = this.httpClient.get<any>('http://127.0.0.1:5000/issue/getById'+id);
        return obj;
    }

    aggiornaIssue(data: any): Observable<any> {
        const headers = new HttpHeaders({
            'Content-Type': 'application/json'
        });

        return this.httpClient.post<any>('http://127.0.0.1:5000/issue/updateIssue', JSON.stringify(data), { headers: headers });
    }

}
