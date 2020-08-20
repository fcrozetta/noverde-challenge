import { Component, OnInit } from '@angular/core';
import { Storage } from '@ionic/storage';
import { NoverdeService } from 'src/app/services/noverde.service';

@Component({
  selector: 'app-loan',
  templateUrl: './loan.page.html',
  styleUrls: ['./loan.page.scss'],
})
export class LoanPage implements OnInit {
  // * Simple object to match the request
  // * In production, please separate model from controller
  newLoanData = {
    // tslint:disable-next-line: object-literal-key-quotes
    'name' : '',
    // tslint:disable-next-line: object-literal-key-quotes
    'cpf': '',
    // tslint:disable-next-line: object-literal-key-quotes
    'birthdate': '',
    // tslint:disable-next-line: object-literal-key-quotes
    'amount': 1000,
    // tslint:disable-next-line: object-literal-key-quotes
    'terms': 6,
    // tslint:disable-next-line: object-literal-key-quotes
    'income': 0
  };

  requests = [];

  fullBirthdate = '';



  constructor(private storage: Storage, private noverde: NoverdeService) { }

  addLoanRequest(){
    this.newLoanData.birthdate = this.fullBirthdate.split('T')[0];
    this.noverde.sendLoanRequest(this.newLoanData).then(data => {
      console.log(data);
    })

  }

  checkRequest(id){
    this.noverde.checkLoanRequest(id);
  }

  ngOnInit() {
    this.storage.get('requests').then(req => {
      this.requests = req;
    });
  }

}
