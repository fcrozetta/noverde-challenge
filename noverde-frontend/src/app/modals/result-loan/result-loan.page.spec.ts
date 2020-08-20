import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { ResultLoanPage } from './result-loan.page';

describe('ResultLoanPage', () => {
  let component: ResultLoanPage;
  let fixture: ComponentFixture<ResultLoanPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ResultLoanPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(ResultLoanPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
