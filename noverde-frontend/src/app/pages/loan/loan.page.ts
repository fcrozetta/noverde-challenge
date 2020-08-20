import { Component, OnInit } from '@angular/core';
import { Storage } from '@ionic/storage';
import { NoverdeService } from 'src/app/services/noverde.service';
import { ModalController } from '@ionic/angular';
import { ResultLoanPage } from '../../modals/result-loan/result-loan.page';

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



  constructor(private storage: Storage, private noverde: NoverdeService, private modalController: ModalController) { }

  addLoanRequest(){
    this.newLoanData.birthdate = this.fullBirthdate.split('T')[0];
    this.noverde.sendLoanRequest(this.newLoanData).then(data => {
      // tslint:disable-next-line: no-string-literal
      const returnedId = data['body']['id'];
      this.requests.push({id: returnedId , name: this.newLoanData.name});
      console.log(this.requests);
      
      this.storage.set('requests', this.requests);
    });

  }

  async checkRequest(id){
    let returnedData = null;
    await this.noverde.checkLoanRequest(id).then(data => {
      console.log(data);
      
      returnedData = {
        'status' : data['body']['status'],
        'result': data['body']['result'],
        'refused_policy': data['body']['refused_policy'],
        'amount': data['body']['amount'],
        'terms': data['body']['terms'],

      }
    });
    const modal = await this.modalController.create({
      component: ResultLoanPage,
      // tslint:disable-next-line: no-string-literal
      componentProps: returnedData
    });
    console.log(returnedData);
    
    modal.present();
  }

  ngOnInit() {
    this.storage.get('requests').then(req => {
      if (req !== null) {
        this.requests = req;
      }
    });
  }

}
