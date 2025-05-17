import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Ponto } from './model/ponto';
import { PontoService } from './service/ponto.service';
import { Espectador } from './model/espectador';
import { EspectadorService } from './service/espectador.service';
import { CommonModule } from '@angular/common'
import { GoogleMapsModule } from '@angular/google-maps';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule, GoogleMapsModule, FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})


export class AppComponent {
  title = 'frontend-app';
  listaPontos: google.maps.LatLngLiteral[] = [];
  center: google.maps.LatLngLiteral = {
    lat: -27.0253683,
    lng: -50.9286241
  };
  novoEspectador: Espectador = new Espectador("", "");
  aceite: boolean = false;

  constructor(private pontoService: PontoService,
            private espectadorService: EspectadorService) { 
    // Add AGM providers at the app component level
  }

  ngOnInit() {
    setInterval(() => {
      this.pontoService.getPontos().then(pontos => {
        this.listaPontos = pontos.map((ponto:Ponto) => ({
          lat: Number(ponto.latitude),
          lng: Number(ponto.longitude)
        }));
      });
    }, 10000);
  }

  salvar(){
    if(this.aceite){
      if(this.novoEspectador.nome == "" || this.novoEspectador.cep == ""){
        alert("Preencha todos os campos.");
        return;
      }
      this.espectadorService.salvar(this.novoEspectador).then(() => {
        alert("Espectador salvo com sucesso!");
        this.novoEspectador = new Espectador("", "");
        this.aceite = false;
      }
      ).catch((error) => {
        console.error("Erro ao salvar ponto:", error);
        alert("Erro ao salvar ponto.");
      }
      );
    }else{
      alert("Você precisa aceitar os termos para continuar.");
    }
    
  }

}
