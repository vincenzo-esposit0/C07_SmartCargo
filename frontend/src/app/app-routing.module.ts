import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import{ HomePageComponent} from "./utente/home-page/home-page.component";
import {AppLayoutComponent} from "./layout/app.layout.component";
import {LoginComponent} from "./autenticazione/login/login.component";
import {GestisciIssueComponent} from "./issue/gestisci-issue/gestisci-issue.component";

const routes: Routes =[
    {
        path: 'home', component:AppLayoutComponent ,
        children: [
            {path: 'dashboard', component: HomePageComponent},
            {path: 'issue', component: GestisciIssueComponent}
        ]
    },
    {path: '', redirectTo: 'login', pathMatch: 'full'},
    {path: 'login', component: LoginComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {


}
