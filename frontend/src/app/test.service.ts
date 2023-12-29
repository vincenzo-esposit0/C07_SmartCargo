import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";

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

}

