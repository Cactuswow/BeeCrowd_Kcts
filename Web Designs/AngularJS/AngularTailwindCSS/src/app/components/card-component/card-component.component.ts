import { Component } from '@angular/core';
import { CardInfo } from './CardInfos';

@Component({
  selector: 'app-card-component',
  templateUrl: './card-component.component.html',
  styleUrls: ['./card-component.component.css'],
})
export class CardComponentComponent {
  CardInfos: CardInfo[] = [];
  DefaultCard: boolean = false;
  bgas:string =
  'https://static.vecteezy.com/system/resources/thumbnails/002/960/590/small/abstract-watercolor-texture-wallpaper-background-free-vector.jpg';

  EliminarTarjeta(i: any) {
    this.CardInfos = this.CardInfos.filter((x) => x != this.CardInfos[i]);
    if (this.CardInfos.length == 0) {
      this.DefaultCard = false;
    }
  }
}
