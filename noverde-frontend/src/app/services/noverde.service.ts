import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Storage } from '@ionic/storage';

@Injectable({
  providedIn: 'root'
})
export class NoverdeService {
  url = 'https://5jnri10wlk.execute-api.us-west-2.amazonaws.com/testing/loan';
  constructor(private http: HttpClient) { }

  sendLoanRequest(data){
    return this.http.post(this.url, data, this.getHeader()).toPromise();
  }

  checkLoanRequest(id: string){
    return this.http.get(`${this.url}/${id}`, this.getHeader()).toPromise();
  }

  getHeader(): object{
    const headers =
    { headers: new HttpHeaders({
        'Content-Type': 'application/json',
        // tslint:disable-next-line: object-literal-key-quotes
        'Accept': '*'
        // tslint:disable-next-line: object-literal-key-quotes
        // , 'Authorization': `Bearer ${token}`
    }) , observe: 'response'};

    return headers;
}
}
