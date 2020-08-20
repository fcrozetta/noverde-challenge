import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    loadChildren: () => import('./pages/loan/loan.module').then( m => m.LoanPageModule)
  },
  {
    path: 'result-loan',
    loadChildren: () => import('./modals/result-loan/result-loan.module').then( m => m.ResultLoanPageModule)
  },
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule {}
