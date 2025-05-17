import { Injectable } from '@angular/core';
import { Ponto } from '../model/ponto';
@Injectable({
  providedIn: 'root'
})
export class PontoService {
  apiURL = "https://qpphi2q647.execute-api.sa-east-1.amazonaws.com/Prod";
  constructor() { }

  getPontos(){
    return fetch(this.apiURL+"/pontos")
      .then(response => response.json())
      .then(data => {
        return data.map((item: any) => {
          return new Ponto(item.cep, item.cidade, item.latitude, item.longitude, item.rua);
        });
      })
      .catch(error => {
        console.error('Error fetching pontos:', error);
        throw error;
      });
  }
}
