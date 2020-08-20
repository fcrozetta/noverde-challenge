import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { LoanPage } from './loan.page';

describe('LoanPage', () => {
  let component: LoanPage;
  let fixture: ComponentFixture<LoanPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LoanPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(LoanPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
