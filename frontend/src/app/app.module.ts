import { NgModule } from '@angular/core';
import {CommonModule, DatePipe} from '@angular/common';

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
import { GestisciIssueComponent } from './issue/gestisci-issue/gestisci-issue.component';
import {DialogModule} from "primeng/dialog";
import {EditorModule} from "primeng/editor";
import {CalendarModule} from "primeng/calendar";
import {AccordionModule} from "primeng/accordion";
import {DividerModule} from "primeng/divider";
import {MultiSelectModule} from "primeng/multiselect";
import {DropdownModule} from "primeng/dropdown";
import { RegistraIngressoComponent } from './ingresso/registra-ingresso/registra-ingresso.component';
import {InputTextareaModule} from "primeng/inputtextarea";
import { SignUpComponent } from './autenticazione/sign-up/sign-up.component';
import { MonitoraggioOperazioniAttiveComponent } from './monitoraggio/monitoraggio-operazioni-attive/monitoraggio-operazioni-attive.component';
import {TableModule} from "primeng/table";
import { DettaglioOperazioneComponent } from './monitoraggio/dettaglio-operazione/dettaglio-operazione.component';
import {GMapModule} from "primeng/gmap";
import {PanelModule} from "primeng/panel";
import {ToolbarModule} from "primeng/toolbar";
@NgModule({
  declarations: [
    AppComponent,
    HomePageComponent,
    LoginComponent,
    GestisciIssueComponent,
    RegistraIngressoComponent,
    SignUpComponent,
    MonitoraggioOperazioniAttiveComponent,
    DettaglioOperazioneComponent
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
        FormsModule,
        DialogModule,
        EditorModule,
        CalendarModule,
        AccordionModule,
        DividerModule,
        MultiSelectModule,
        DropdownModule,
        InputTextareaModule,
        TableModule,
        GMapModule,
        PanelModule,
        ToolbarModule
    ],
  providers: [MessageService, DatePipe],
  bootstrap: [AppComponent]
})
export class AppModule { }
