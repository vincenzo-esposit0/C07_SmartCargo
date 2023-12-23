import { NgModule } from '@angular/core';
import {CommonModule} from '@angular/common';

import { BrowserModule } from '@angular/platform-browser';
import {AppLayoutModule} from "./layout/app.layout.module";
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomePageComponent } from './utente/home-page/home-page.component';
import { LoginComponent } from './autenticazione/login/login.component';
import {InputTextModule} from "primeng/inputtext";
import {PasswordModule} from "primeng/password";
import {ButtonModule} from "primeng/button";
import {ToastModule} from "primeng/toast";
import { FormsModule } from '@angular/forms';
import {MessageService} from "primeng/api";

@NgModule({
  declarations: [
    AppComponent,
    HomePageComponent,
    LoginComponent
  ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        AppLayoutModule,
        InputTextModule,
        PasswordModule,
        ButtonModule,
        ToastModule,
        CommonModule,
        FormsModule
    ],
  providers: [MessageService],
  bootstrap: [AppComponent]
})
export class AppModule { }
