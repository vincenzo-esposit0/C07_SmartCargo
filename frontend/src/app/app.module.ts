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

import { StoricoOperazioniComponent } from './monitoraggio/storico-operazioni/storico-operazioni.component';
import {QRCodeModule} from "angularx-qrcode";
import {AgmCoreModule} from "@agm/core";
import {MenuModule} from "primeng/menu";
import {ChartModule} from "primeng/chart";
import { MonitoraggioOperazioniCaricoScaricoComponent } from './monitoraggio/monitoraggio-operazioni-carico-scarico/monitoraggio-operazioni-carico-scarico.component';
import {ConfirmDialogModule} from "primeng/confirmdialog";
import {EditProfiloComponent} from "./utente/edit-profilo/edit-profilo.component";
@NgModule({
    declarations: [
        AppComponent,
        HomePageComponent,
        LoginComponent,
        GestisciIssueComponent,
        RegistraIngressoComponent,
        SignUpComponent,
        MonitoraggioOperazioniAttiveComponent,
        DettaglioOperazioneComponent,
        StoricoOperazioniComponent,
        MonitoraggioOperazioniCaricoScaricoComponent,
        StoricoOperazioniComponent,
        EditProfiloComponent
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
        ToolbarModule,
        AgmCoreModule.forRoot({
            apiKey: 'AIzaSyC8RUeomWkI3pS7yRcVvIpM4DM7GpRpiqo',
        }),
        MenuModule,
        ChartModule,
        ToolbarModule,
        QRCodeModule,
        ConfirmDialogModule
    ],
    providers: [MessageService, DatePipe],
    bootstrap: [AppComponent]
})
export class AppModule { }
