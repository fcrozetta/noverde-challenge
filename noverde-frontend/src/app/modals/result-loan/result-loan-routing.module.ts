import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ResultLoanPage } from './result-loan.page';

const routes: Routes = [
  {
    path: '',
    component: ResultLoanPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ResultLoanPageRoutingModule {}
