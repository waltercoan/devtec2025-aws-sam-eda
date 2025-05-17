import { Injectable } from '@angular/core';
import { Espectador } from '../model/espectador';

@Injectable({
  providedIn: 'root'
})
export class EspectadorService {
  apiURL = "https://qpphi2q647.execute-api.sa-east-1.amazonaws.com/Prod";
  constructor() { }

  salvar(espectador: Espectador) {
    return fetch(this.apiURL+"/espectadores", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(espectador)
    })
    .then(response => {
      console.error('Retorno do servidor:', response);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .catch(error => {
      console.error('Error saving espectador:', error);
      throw error;
    });
  }
}
