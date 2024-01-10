import {ChangeDetectorRef, Component} from '@angular/core';
import {Router} from "@angular/router";
import {ConfirmationService, MessageService} from "primeng/api";
import {DatePipe} from "@angular/common";
import {IssueService} from "../../issue/issue.service";

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



    constructor(private confirm: ConfirmationService,private issueService: IssueService,private datePipe: DatePipe,private router: Router,private messageService: MessageService, private cdr: ChangeDetectorRef) {
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
            zoom: 15,
        };

        /*
        this.data.percorso.puntiLatitudineCorretti = "39.4542,39.45473,39.45532,39.45606,39.45433,39.45372,39.45352,39.45272,39.45185," +
            "39.45109,39.45095,39.45058,39.44984,39.44952,39.4486,39.44768,39.44675,39.44582,39.445," +
            "39.44459,39.44439,39.44418,39.44393,39.44329,39.4422,39.44083,39.43942,39.43757,39.43574," +
            "39.4341,39.43264,39.43153,39.4311,39.43089,39.43063,39.43005,39.42885,39.42821,39.429," +
            "39.42992,39.43079,39.43163,39.43257,39.43348,39.43432,39.43505,39.43543,39.43465,39.4333," +
            "39.43209,39.43164,39.43165,39.43174,39.4311,39.43045,39.4298,39.42909,39.42827,39.42735," +
            "39.42657,39.42575,39.42553,39.42599,39.42706,39.42829,39.42948,39.43006,39.43046,39.43063," +
            "39.4316,39.43246,39.43138,39.42986,39.42832,39.42733,39.42679,39.42619,39.42562,39.42511," +
            "39.42456,39.42392,39.42328,39.42323,39.42421,39.42577,39.42745,39.42908,39.43015,39.43027," +
            "39.42921,39.42766,39.42598,39.42456,39.42414,39.42361,39.42345,39.42355,39.42415,39.42473," +
            "39.42526,39.42582,39.42643,39.42704,39.42764,39.4288,39.42994,39.43108,39.43198,39.43329," +
            "39.4346,39.43587,39.4373,39.43878,39.44029,39.44181,39.44298,39.44336,39.44398,39.4446,39.4451," +
            "39.44602,39.44748,39.44895,39.44987,39.45042,39.4516,39.45288,39.45437,39.45555,39.45652," +
            "39.45785,39.45914,39.46003,39.46002,39.4592,39.45786,39.4564,39.45555,39.45459,39.4533," +
            "39.45225,39.45152,39.45091,39.45074,39.45074,39.45057,39.45065,39.45081,39.45081,39.45081," +
            "39.45087,39.45149,39.45254,39.4537,39.45464,39.45497,39.4553,39.45576,39.45615,39.45724," +
            "39.45845,39.45958,39.4602,39.46007,39.45917,39.45802,39.45684,39.45574,39.45479,39.45366," +
            "39.45228,39.45105,39.45033,39.44974,39.45058";
            this.data.percorso.puntiLongitudineCorretti =  "-0.32866,-0.3289,-0.32874,-0.32999,-0.32921," +
                "-0.32923,-0.32923,-0.32896,-0.32867,-0.32853,-0.32852,-0.32855,-0.32876,-0.32776,-0.32715," +
                "-0.32696,-0.32682,-0.32679,-0.32731,-0.32834,-0.32887,-0.32932,-0.32997,-0.33042,-0.33132," +
                "-0.3325,-0.33361,-0.33434,-0.33442,-0.33451,-0.33507,-0.33546,-0.33549,-0.3355,-0.33549," +
                "-0.33552,-0.33548,-0.34008,-0.34232,-0.34473,-0.34713,-0.34946,-0.35189,-0.35432,-0.35656," +
                "-0.35815,-0.35749,-0.35758,-0.35838,-0.3591,-0.35903,-0.35796,-0.35697,-0.35514,-0.35325," +
                "-0.35136,-0.34925,-0.34694,-0.34427,-0.3421,-0.34063,-0.33882,-0.33706,-0.33582,-0.33538," +
                "-0.33518,-0.33512,-0.33511,-0.33508,-0.33508,-0.33413,-0.33109,-0.32921,-0.32841,-0.32726," +
                "-0.32548,-0.32365,-0.3218,-0.32007,-0.31851,-0.31652,-0.31457,-0.31345,-0.31259,-0.31174," +
                "-0.31083,-0.30993,-0.30952,-0.31004,-0.30996,-0.31085,-0.31175,-0.31252,-0.31276,-0.31319," +
                "-0.31392,-0.31514,-0.317,-0.31877,-0.32043,-0.32218,-0.324,-0.32591,-0.32765,-0.3281," +
                "-0.32896,-0.33,-0.33162,-0.33276,-0.33362,-0.3342,-0.33421,-0.3338,-0.3328,-0.33148," +
                "-0.33042,-0.32975,-0.32938,-0.328,-0.3265,-0.32652,-0.32678,-0.32719,-0.32787,-0.3282," +
                "-0.32835,-0.32876,-0.3292,-0.32797,-0.3265,-0.32511,-0.32371,-0.32206,-0.32006,-0.31838," +
                "-0.31737,-0.31636,-0.31556,-0.31507,-0.31418,-0.31316,-0.31319,-0.31242,-0.31101,-0.30946," +
                "-0.30827,-0.30769,-0.30884,-0.30884,-0.31031,-0.31193,-0.31309,-0.31328,-0.31436,-0.31502," +
                "-0.31518,-0.31481,-0.31511,-0.31603,-0.31682,-0.31768,-0.31874,-0.32041,-0.32233,-0.32386," +
                "-0.32506,-0.32629,-0.32752,-0.32861,-0.32998,-0.32871,-0.32845,-0.3287,-0.3284,-0.32825," +
                "-0.32831,-0.32866,-0.32884,-0.329,-0.32846,-0.3287,-0.32877";


         */

        this.data.percorso.puntiLongitudineCorretti = this.data.percorso.puntiLongitudinePercorsi;
        this.data.percorso.puntiLatitudineCorretti = this.data.percorso.puntiLatitudinePercorsi;


        this.aggiungiPuntoOgni2Secondi();
    }



    aggiungiPuntoOgni2Secondi() {
        this.intervalId = setInterval(() => {
            const latPercorso = Number(this.data.percorso.puntiLatitudinePercorsi.split(',')[this.index]);
            const lngPercorso = Number(this.data.percorso.puntiLongitudinePercorsi.split(',')[this.index]);
            const latCorretto = Number(this.data.percorso.puntiLatitudineCorretti.split(',')[this.index]);
            const lngCorretto = Number(this.data.percorso.puntiLongitudineCorretti.split(',')[this.index]);

            // Verifica se i punti corrispondono
            const corrispondenza = latPercorso === latCorretto && lngPercorso === lngCorretto;

            if(corrispondenza){
                // Creazione marker per il percorso
                const markerPercorso = this.creaMarkerDaDati(latPercorso, lngPercorso, 'Punto ' + (this.index + 1) + ' Percorso', corrispondenza ? 'blue' : 'red');
                this.overlays.push(markerPercorso);
            }
            else {
                // Creazione marker per il percorso
                const markerPercorso = this.creaMarkerDaDati(latPercorso, lngPercorso, 'Punto ' + (this.index + 1) + ' Percorso', corrispondenza ? 'blue' : 'red');
                this.overlays.push(markerPercorso);

                // Creazione marker per il punto corretto
                const markerCorretto = this.creaMarkerDaDati(latCorretto, lngCorretto, 'Punto ' + (this.index + 1) + ' Corretto', 'green');
                this.overlays.push(markerCorretto);
            }




            this.index++;

            if (this.index >= this.data.percorso.puntiLatitudinePercorsi.split(',').length) {
                clearInterval(this.intervalId); // Fermare il setInterval quando tutti i punti sono stati aggiunti
            }

            if (this.overlays.length >= 5) {
                this.creaPolilineaDaPuntiVerdi();
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
                if (mk1.icon.fillColor === 'blue' && mk2.icon.fillColor === 'blue') {
                    nuovePolilinee.push(this.creaPolyline([mk1.getPosition(), mk2.getPosition()], 'blue'));
                }
                else{
                    //da blue a rosso linea rossa
                    if (mk1.icon.fillColor === 'blue' && mk2.icon.fillColor === 'red') {
                        nuovePolilinee.push(this.creaPolyline([mk1.getPosition(), mk2.getPosition()], 'red'));
                    }
                    else {
                        //da rosso a blue linea rossa
                        if (mk1.icon.fillColor === 'red' && mk2.icon.fillColor === 'blue') {
                            nuovePolilinee.push(this.creaPolyline([mk1.getPosition(), mk2.getPosition()], 'red'));
                        }
                        else {
                            //da verde a blue linea verde
                            if (mk1.icon.fillColor === 'green' && mk2.icon.fillColor === 'blue') {
                                nuovePolilinee.push(this.creaPolyline([mk1.getPosition(), mk2.getPosition()], 'green'));
                            }
                            else {
                                if (mk1.icon.fillColor === 'blue' && mk2.icon.fillColor === 'green') {
                                    nuovePolilinee.push(this.creaPolyline([mk1.getPosition(), mk2.getPosition()], 'green'));
                                }
                                else{
                                    if (mk1.icon.fillColor === 'red' && mk2.icon.fillColor === 'blue') {
                                        nuovePolilinee.push(this.creaPolyline([mk1.getPosition(), mk2.getPosition()], 'red'));
                                    }
                                }
                            }

                        }
                    }
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
                    this.messageService.add({ severity: 'success', summary: 'Attenzione', detail: 'Operazione avvenuta con successo!' });

                },error => {
                    this.messageService.add({ severity: 'error', summary: 'Attenzione', detail: 'Errore durante la chiusura dell\'issue' });

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

}
