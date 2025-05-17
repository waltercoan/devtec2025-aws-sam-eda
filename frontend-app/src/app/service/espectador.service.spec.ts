import { TestBed } from '@angular/core/testing';

import { EspectadorService } from './espectador.service';

describe('EspectadorService', () => {
  let service: EspectadorService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EspectadorService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
