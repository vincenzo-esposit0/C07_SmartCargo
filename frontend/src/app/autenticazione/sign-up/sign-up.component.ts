import { Component } from '@angular/core';
import { Router } from "@angular/router";
import { AutenticazioneService } from "../autenticazione.service";
import { DatePipe } from "@angular/common";
import { MessageService } from "primeng/api";

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.scss']
})
export class SignUpComponent {

  constructor(
    private messageService: MessageService,
    private datePipe: DatePipe,
    private router: Router,
    private autenticazioneService: AutenticazioneService
  ) {}

  autotrasportatore: any = {};

  calcolaEta(dataNascita: Date): number {
    const oggi = new Date();
    const dataNascitaDate = new Date(dataNascita);
    const differenzaAnni = oggi.getFullYear() - dataNascitaDate.getFullYear();

    if (
      oggi.getMonth() < dataNascitaDate.getMonth() ||
      (oggi.getMonth() === dataNascitaDate.getMonth() && oggi.getDate() < dataNascitaDate.getDate())
    ) {
      return differenzaAnni - 1; // Sottrai uno se l'utente non ha ancora compiuto l'anno
    } else {
      return differenzaAnni;
    }
  }

  checkFormValidity(): boolean {
    const nomeRegex = /^[a-zA-Z\s.'-]{2,30}$/;
    const cognomeRegex = /^[a-zA-Z\s.'-]{2,30}$/;
    const codiceFiscaleRegex = /^[A-Z]{6}\d{2}[ABCDEHLMPRST]\d{02}[A-Z]\d{03}[A-Z]$/;
    const emailRegex = /^[A-z0-9._%+-]+@[A-z0-9.-]+\.[A-z]{2,10}$/;
    const indirizzoRegex = /^([a-zA-Zà-úÀ-Ú0-9\s.'-]+),\s*(\d+),\s*([a-zA-Zà-úÀ-Ú\s.'-]+),\s*([0-9]{5})$/;
    const aziendaRegex = /^[a-zA-Z0-9\s.'-]{3,30}$/;
    const passwordRegex = /^.{8,}$/;

    if (!nomeRegex.test(this.autotrasportatore.nome)) {
      this.messageService.add({ severity: 'error', summary: 'Errore', detail: 'Nome non valido' });
      return false;
    }

    if (!cognomeRegex.test(this.autotrasportatore.cognome)) {
      this.messageService.add({ severity: 'error', summary: 'Errore', detail: 'Cognome non valido' });
      return false;
    }

    if (!aziendaRegex.test(this.autotrasportatore.azienda)) {
      this.messageService.add({ severity: 'error', summary: 'Errore', detail: 'Azienda non valida' });
      return false;
    }

    if (!codiceFiscaleRegex.test(this.autotrasportatore.codiceFiscale)) {
      this.messageService.add({ severity: 'error', summary: 'Errore', detail: 'Codice Fiscale non valido' });
      return false;
    }

    if (!indirizzoRegex.test(this.autotrasportatore.indirizzo)) {
      this.messageService.add({ severity: 'error', summary: 'Errore', detail: 'Indirizzo non valido' });
      return false;
    }

    if (!emailRegex.test(this.autotrasportatore.email)) {
      this.messageService.add({ severity: 'error', summary: 'Errore', detail: 'Email non valida' });
      return false;
    }

    if (!passwordRegex.test(this.autotrasportatore.password)) {
      this.messageService.add({ severity: 'error', summary: 'Errore', detail: 'Password non valida' });
      return false;
    }

    // Verifica dell'età
    if (!this.autotrasportatore.dataNascita || this.calcolaEta(this.autotrasportatore.dataNascita) < 18) {
      this.messageService.add({ severity: 'error', summary: 'Errore', detail: 'L\'utente deve avere almeno 18 anni' });
      return false;
    }

    return true;
  }

  inserisci() {
    if (this.checkFormValidity()) {
      this.autotrasportatore.dataNascita = this.datePipe.transform(this.autotrasportatore.dataNascita, 'yyyy-MM-ddTHH:mm:ss');
      this.autenticazioneService.registrazione(this.autotrasportatore).subscribe(dati => {
        let value = dati;
        // Todo: controlla se lo stato è corretto
        if (this.autotrasportatore.email && this.autotrasportatore.password && !this.autenticazioneService.profile) {
          this.autenticazioneService.profile = {};
          let profilo = { username: "", password: "" };
          profilo.username = this.autotrasportatore.email;
          profilo.password = this.autotrasportatore.password;
          this.autenticazioneService.login(profilo).subscribe(dati => {
            let value = dati;
            if (value.stato == 200) {
              this.autenticazioneService.profile.username = this.autotrasportatore.email;
              this.autenticazioneService.profile.password = this.autotrasportatore.password;
              this.autenticazioneService.profile.operatore = value.operatore;
              this.router.navigate(['home']);
            } else {
              this.messageService.add({ severity: 'error', summary: 'Login', detail: value.message });
            }
          }, error => {
            console.log(error);
          });
        }
        /* if(value.stato==200){

                     this.autenticazioneService.profile.operatore=value.operatore;
                     this.router.navigate(['home']);
                 }else{
                     this.messageService.add({ severity: 'error', summary: 'Login', detail: value.message });
                 }*/
      }, error => {
        console.log(error);
      });
    }
  }
}
