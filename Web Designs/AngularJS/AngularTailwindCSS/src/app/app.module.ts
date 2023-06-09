import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CardComponentComponent } from './components/card-component/card-component.component';
import { FibonacciComponent } from './components/fibonacci/fibonacci.component';

@NgModule({
  declarations: [
    AppComponent,
    CardComponentComponent,
    FibonacciComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
