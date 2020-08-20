import { Component, OnInit, Input } from '@angular/core';
import { ModalController } from '@ionic/angular';

@Component({
  selector: 'app-result-loan',
  templateUrl: './result-loan.page.html',
  styleUrls: ['./result-loan.page.scss'],
})
export class ResultLoanPage implements OnInit {

  @Input() status;
  @Input() result;
  @Input() refused_policy;
  @Input() amount;
  @Input() terms;

  constructor(private modalController: ModalController) { }

  dismiss(){
    this.modalController.dismiss();
  }

  ngOnInit() {
    console.log(this.status);
  }

}
