import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class UtenteService {

    constructor(private httpClient: HttpClient) { }


    getAutotrasportatoreById(id: string): Observable<any>{
        const obj = this.httpClient.get<any>('http://127.0.0.1:5000/autotrasportatore/getById/'+id);
        return obj;
    }
}
