import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import{ HomePageComponent} from "./utente/home-page/home-page.component";
import {AppLayoutComponent} from "./layout/app.layout.component";
import {LoginComponent} from "./autenticazione/login/login.component";
import {GestisciIssueComponent} from "./issue/gestisci-issue/gestisci-issue.component";
import {RegistraIngressoComponent} from "./ingresso/registra-ingresso/registra-ingresso.component";
import {SignUpComponent} from "./autenticazione/sign-up/sign-up.component";
import {MonitoraggioOperazioniAttiveComponent} from "./monitoraggio/monitoraggio-operazioni-attive/monitoraggio-operazioni-attive.component";
import {DettaglioOperazioneComponent} from "./monitoraggio/dettaglio-operazione/dettaglio-operazione.component";

const routes: Routes =[
    {
        path: 'home', component:AppLayoutComponent ,
        children: [
            {path: 'dashboard', component: HomePageComponent},
            {path: 'issue', component: GestisciIssueComponent},
            {path: 'ingresso', component: RegistraIngressoComponent},
            {path: 'monitoraggioOpAttive', component: MonitoraggioOperazioniAttiveComponent},
            {path: 'dettaglioOp', component: DettaglioOperazioneComponent}
        ]
    },
    {path: '', redirectTo: 'login', pathMatch: 'full'},
    {path: 'login', component: LoginComponent},
    {path: 'registrati', component: SignUpComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {


}
