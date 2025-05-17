import { TestBed } from '@angular/core/testing';

import { PontoService } from './ponto.service';

describe('PontoService', () => {
  let service: PontoService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PontoService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
