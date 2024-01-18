import {ChangeDetectorRef, Component} from '@angular/core';
import {Router} from "@angular/router";
import {ConfirmationService, MessageService} from "primeng/api";
import {DatePipe} from "@angular/common";
import {IssueService} from "../../issue/issue.service";
import {AutenticazioneService} from "../../autenticazione/autenticazione.service";

@Component({
  selector: 'app-dettaglio-operazione',
  templateUrl: './dettaglio-operazione.component.html',
  styleUrls: ['./dettaglio-operazione.component.scss'],
    providers: [MessageService, ConfirmationService]
})
export class DettaglioOperazioneComponent {

    data: any = {};
    options: any;
    infoWindow: any = {};
    index: any = 0;
    intervalId: any = 0;

    content: any[] = [
        {icon: 'pi pi-fw pi-phone', title: 'Telefono', info:''},
        {icon: 'pi pi-fw pi-map-marker', title: 'Il nostro Ufficio', info: ''},
        {icon: 'pi pi-fw pi-print', title: 'Fax', info:+''}
    ];

    showDialog: boolean = false;

    //solo se nn ci sono già issue aperte sull'operazione
    showNewIssue : boolean = true;
    noIssue: boolean = false;
    overlays: any[] = [];
    showDialogAnomalia: boolean = false;
    datiAnomalia: any = {}

    puntiLatErrati: number[] = [];
    puntiLngErrati: number[] = [];
    disableAll: boolean = false;



    constructor(public autenticazioneService : AutenticazioneService,private confirm: ConfirmationService,private issueService: IssueService,private datePipe: DatePipe,private router: Router,public messageService: MessageService, private cdr: ChangeDetectorRef) {
        if (this.router.getCurrentNavigation()?.extras.state) {
            // @ts-ignore
            let routeState = this.router.getCurrentNavigation().extras.state;
            if (routeState) {
                // @ts-ignore
                this.data = routeState.dataJson;
            }
        }
    }


    ngOnInit(){
        this.infoWindow = new google.maps.InfoWindow();

        let latitude = 39.4542;
        let longitude = -0.32866;

        if(this.data){
            if(this.data.issue){
                if(this.data.issue?.stato == 'Aperta'){
                    this.showNewIssue = false;
                }
                else if(this.data.issue?.stato == 'Chiusa' || this.data.issue?.stato == 'Chiuso'){
                    this.noIssue = true;
                }
            }
            else this.data.issue = {};
        }


        this.options = {
            center: {lat: latitude, lng: longitude},
            zoom: 13,
        };

        this.puntiLatErrati = this.data.percorso.puntiLatitudineErrati.split(',');
        this.puntiLngErrati = this.data.percorso.puntiLongitudineErrati.split(',');


        if(!this.data.fromStorico && this.autenticazioneService?.profile?.operatore!=='Autotrasportatore') //this.creaTuttoPercorso()
            this.aggiungiPuntoOgni2Secondi();

        else this.creaTuttoPercorso();
    }



    aggiungiPuntoOgni2Secondi() {
        this.datiAnomalia = {};
        this.intervalId = setInterval(() => {
            const latPercorso = Number(this.data.percorso.puntiLatitudinePercorsi.split(',')[this.index]);
            const lngPercorso = Number(this.data.percorso.puntiLongitudinePercorsi.split(',')[this.index]);

            let corretto = true;

            for(let lat of this.puntiLatErrati){
                if(Number(lat) == latPercorso) corretto = false;
            }

            for(let lng of this.puntiLngErrati){
                if(Number(lng) == lngPercorso) corretto = false;
            }

            if(this.autenticazioneService?.profile?.operatore!=='Autotrasportatore'){
                if(corretto){
                    // Creazione marker per il percorso
                    const markerPercorso = this.creaMarkerDaDati(latPercorso, lngPercorso, 'Punto ' + (this.index + 1) + ' Percorso', 'green');
                    this.overlays.push(markerPercorso);
                }
                else {

                    if(!this.showDialogAnomalia){
                        this.showDialogAnomalia = true;
                        this.datiAnomalia = {
                            lat : latPercorso,
                            lng: lngPercorso
                        }
                        this.messageService.add({ key: 'confirm', sticky: true, severity: 'error', summary: 'Can you send me the report?' });
                    }

                    // Creazione marker per il punto errato
                    const markerCorretto = this.creaMarkerDaDati(latPercorso, lngPercorso, 'Punto ' + (this.index + 1) + ' Anomalo', 'red');
                    this.overlays.push(markerCorretto);
                }
            }
            else {
                const markerPercorso = this.creaMarkerDaDati(latPercorso, lngPercorso, 'Punto ' + (this.index + 1) + ' Percorso', 'blue');
                this.overlays.push(markerPercorso);
            }



            this.index++;

            if (this.index >= this.data.percorso.puntiLatitudinePercorsi.split(',').length) {
                clearInterval(this.intervalId); // Fermare il setInterval quando tutti i punti sono stati aggiunti
            }

            if (this.overlays.length >= 3) {
                //this.creaPolilineaDaPuntiVerdi();
            }

            this.cdr.detectChanges(); // Forzare l'aggiornamento della vista
        }, 100);
    }

    creaPolilineaDaPuntiVerdi(): void {
        // Filtra solo le polilinee dall'array
        const polilineeEsistenti = this.overlays.filter(overlay => overlay instanceof google.maps.Polyline);

        // Rimuovi le polilinee esistenti dall'array principale
        this.overlays = this.overlays.filter(overlay => !(overlay instanceof google.maps.Polyline));

        const nuovePolilinee = [];

        for (let i = 0; i < this.overlays.length - 1; ++i) {
            let mk1 = this.overlays[i];
            let mk2 = this.overlays[i + 1];

            if (mk1 && mk2 && mk1.icon && mk2.icon) {
                //da blue a blue linea blu
                if (mk1.icon.fillColor === 'green' && mk2.icon.fillColor === 'red') {
                    nuovePolilinee.push(this.creaPolyline([mk1.getPosition(), mk2.getPosition()], 'red'));
                }
                if (mk1.icon.fillColor === 'green' && mk2.icon.fillColor === 'green') {
                    nuovePolilinee.push(this.creaPolyline([mk1.getPosition(), mk2.getPosition()], 'green'));
                }
                if (mk1.icon.fillColor === 'red' && mk2.icon.fillColor === 'green') {
                    nuovePolilinee.push(this.creaPolyline([mk1.getPosition(), mk2.getPosition()], 'red'));
                }
                if (mk1.icon.fillColor === 'red' && mk2.icon.fillColor === 'red') {
                    nuovePolilinee.push(this.creaPolyline([mk1.getPosition(), mk2.getPosition()], 'red'));
                }
                if (mk1.icon.fillColor === 'blue' && mk2.icon.fillColor === 'blue') {
                    nuovePolilinee.push(this.creaPolyline([mk1.getPosition(), mk2.getPosition()], 'blue'));
                }

            }
        }

        // Aggiungi le nuove polilinee all'array principale
        this.overlays = this.overlays.concat(nuovePolilinee, polilineeEsistenti);

        // Aggiorna la vista
        this.cdr.detectChanges();
    }


    creaPolyline(path: google.maps.LatLngLiteral[], color: string) {
        const polyline = new google.maps.Polyline({
            path: path,
            geodesic: true,
            strokeColor: color,
            strokeOpacity: 0.5,
            strokeWeight: 2
        });
        return polyline;
    }


    creaMarkerDaDati(lat: number, lng: number, title: string, colore: string) {
        const marker = new google.maps.Marker({
            position: { lat, lng },
            title,
            icon: {
                path: google.maps.SymbolPath.CIRCLE,
                scale: 8,
                fillColor: colore,
                fillOpacity: 1,
                strokeColor: '#FFFFFF',
                strokeWeight: 2
            }
        });
        return marker;
    }


    newIssue() {
        this.showDialog = true;
    }

    aggiornaIssue() {
        this.showDialog = true;
    }


    chiudiIssue() {
        this.confirm.confirm({
            message: 'Sei sicuro di voler chiudere l\' issue?',
            header: 'Attenzione',
            icon: 'pi pi-exclamation-triangle',
            acceptLabel: 'Si',
            accept: () => {
                this.data.issue.stato = "Chiusa";
                console.log(this.data.issue.timestampApertura);
                this.data.issue.timestampApertura = this.datePipe.transform(this.data.issue.timestampApertura, 'yyyy-MM-ddTHH:mm:ss');
                this.data.issue.timestampChiusura = this.datePipe.transform(this.data.issue.timestampApertura, 'yyyy-MM-ddTHH:mm:ss');
                this.data.issue.tipologiaProblema = this.data.issue.tipologiaProblema.nome
                this.issueService.aggiornaIssue(this.data.issue).subscribe(dati => {
                    this.disableAll = true;
                    this.messageService.add({ severity: 'success', summary: 'Attenzione', detail: 'Operazione avvenuta con successo!' });

                },error => {
                    this.disableAll = true;
                });
            },
            reject: () => {

            }
        });

    }

    handleOverlayClick(event : any) {
        let isMarker = event.overlay.getTitle != undefined;

        if (isMarker) {
            let title = event.overlay.getTitle();
            this.infoWindow.setContent('' + title + '');
            this.infoWindow.open(event.map, event.overlay);
            event.map.setCenter(event.overlay.getPosition());

            this.messageService.add({severity:'info', summary:'Marker Selected', detail: title});
        }
        else {
            this.messageService.add({severity:'info', summary:'Shape Selected', detail: ''});
        }
    }

    creaTuttoPercorso() {
        this.datiAnomalia = {};

        const latitudini = this.data.percorso.puntiLatitudinePercorsi.split(',');
        const longitudini = this.data.percorso.puntiLongitudinePercorsi.split(',');

        for (let i = 0; i < latitudini.length; i++) {
            const latPercorso = Number(latitudini[i]);
            const lngPercorso = Number(longitudini[i]);

            const markerPercorso = this.creaMarkerDaDati(latPercorso, lngPercorso, 'Punto ' + (i + 1) + ' Percorso', 'green');
            this.overlays.push(markerPercorso);

            /*
            let corretto = true;

            for (let lat of this.puntiLatErrati) {
                if (Number(lat) === latPercorso) {
                    corretto = false;
                }
            }

            for (let lng of this.puntiLngErrati) {
                if (Number(lng) === lngPercorso) {
                    corretto = false;
                }
            }


            if (this.autenticazioneService?.profile?.operatore !== 'Autotrasportatore') {
                if (corretto) {
                    // Creazione marker per il percorso
                    const markerPercorso = this.creaMarkerDaDati(latPercorso, lngPercorso, 'Punto ' + (i + 1) + ' Percorso', 'green');
                    this.overlays.push(markerPercorso);
                } else {
                    if (!this.showDialogAnomalia && false) {
                        this.showDialogAnomalia = true;
                        this.datiAnomalia = {
                            lat: latPercorso,
                            lng: lngPercorso
                        };
                    }

                    // Creazione marker per il punto errato
                    const markerCorretto = this.creaMarkerDaDati(latPercorso, lngPercorso, 'Punto ' + (i + 1) + ' Anomalo', 'red');
                    this.overlays.push(markerCorretto);
                }
            } else {
                const markerPercorso = this.creaMarkerDaDati(latPercorso, lngPercorso, 'Punto ' + (i + 1) + ' Percorso', 'blue');
                this.overlays.push(markerPercorso);
            }

             */
        }

        // Creazione polilinea
        this.creaPolilineaDaPuntiVerdi();

        this.cdr.detectChanges(); // Forzare l'aggiornamento della vista
    }

    chiamaAutorita() {
        this.confirm.confirm({
            message: 'Sei sicuro di voler chiamare le autorità competenti?',
            header: 'Attenzione',
            icon: 'pi pi-exclamation-triangle',
            acceptLabel: 'Si',
            accept: () => {

                this.messageService.add({ severity: 'warn', summary: 'Attenzione!', detail: 'Segnalazione inviata alle autorità competenti!' });
            },
            reject: () => {

            }
        });



    }
}
