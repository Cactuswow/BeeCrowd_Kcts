import { Component, ViewChild } from '@angular/core';
import { CardComponentComponent } from './components/card-component/card-component.component';
import { CardInfo } from './components/card-component/CardInfos';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  @ViewChild(CardComponentComponent) CardComponent: any;

  EnviarDatos() {
    let InputsData = document.querySelectorAll('input');
    let CardInfoJson: CardInfo = {
      name: InputsData[0].value,
      desc: InputsData[1].value,
      rating: parseFloat(InputsData[2].value),
    };

    this.ValidarDatos(CardInfoJson);
  }

  ValidarDatos(CardInfoJson: CardInfo) {
    let ValidName = CardInfoJson.name.trim().length == 0;
    let ValidDesc = CardInfoJson.desc.trim().length == 0;
    let ValidRating = isNaN(CardInfoJson.rating);
    let ValidRange = CardInfoJson.rating > 5 || CardInfoJson.rating < 1;

    if (!ValidName && !ValidDesc && !ValidRating && !ValidRange) {
      this.AgregarElemento(CardInfoJson);
    }

    if (ValidName || ValidDesc || ValidRating) {
      alert('Sin valores en blanco, porfa \nKactuswow');
    }

    if (ValidRange) {
      alert('Error, raiting de 1 - 5 estrellas');
    }
  }

  AgregarElemento(CardInfoJson: CardInfo) {
    this.CardComponent.DefaultCard = true;
    this.CardComponent.CardInfos.push(CardInfoJson);
  }
}
