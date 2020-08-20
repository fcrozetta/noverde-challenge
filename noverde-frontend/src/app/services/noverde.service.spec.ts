import { TestBed } from '@angular/core/testing';

import { NoverdeService } from './noverde.service';

describe('NoverdeService', () => {
  let service: NoverdeService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(NoverdeService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
