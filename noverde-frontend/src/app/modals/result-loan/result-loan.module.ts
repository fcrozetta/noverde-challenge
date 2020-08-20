import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { ResultLoanPageRoutingModule } from './result-loan-routing.module';

import { ResultLoanPage } from './result-loan.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    ResultLoanPageRoutingModule
  ],
  declarations: [ResultLoanPage]
})
export class ResultLoanPageModule {}
