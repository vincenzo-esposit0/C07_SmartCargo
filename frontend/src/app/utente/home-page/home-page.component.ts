import { Component } from '@angular/core';
import {AppConfig} from "../../layout/service/app.layout.service";
import {Table} from "primeng/table";
import {Subscription} from "rxjs";
import {MenuItem} from "primeng/api";

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss']
})
export class HomePageComponent {

    subscription!: Subscription;

    items: MenuItem[] = [];

    ordersChart: any;

    ordersChartOptions: any;

    revenueChart: any;

    revenueChartOptions: any;

    cols: any[] = [];

    config!: AppConfig;

    orderWeek: any[] = [];

    metrics: any[] = [];

    teamMembers: any[] = [];

    selectedOrderWeek!: any;


    constructor() {}


    ngOnInit() {
        this.cols = [
            {field: 'vin', header: 'Vin'},
            {field: 'year', header: 'Year'},
            {field: 'brand', header: 'Brand'},
            {field: 'color', header: 'Color'}
        ];

        this.items = [
            {
                label: 'Shipments',
                items: [
                    { label: 'Tracker', icon: 'pi pi-compass' },
                    { label: 'Map', icon: 'pi pi-map-marker' },
                    { label: 'Manage', icon: 'pi pi-pencil' }
                ]
            }
        ];

        this.orderWeek = [
            {name: 'This Week', code: '0'},
            {name: 'Last Week', code: '1'}
        ];

        this.metrics = [
            {
                title: 'Operatori',
                icon: 'pi pi-user',
                color_light: '#64B5F6',
                color_dark: '#1976D2',
                textContent: [
                    {amount: '20', text: 'Attivi'},
                    {amount: '100', text: 'Totali'}
                ]
            },
            {
                title: 'Autotrasportatori',
                icon: 'pi pi-truck',
                color_light: '#7986CB',
                color_dark: '#303F9F',
                textContent: [
                    {amount: '50', text: 'Attivi'},
                    {amount: '1000', text: 'Registrati'}
                ]
            },
            {
                title: 'Issue',
                icon: 'pi pi-truck',
                color_light: '#4DB6AC',
                color_dark: '#00796B',
                textContent: [
                    {amount: 10, text: 'Aperte'},
                    {amount: 200, text: 'Totali'}
                ]
            },
            {
                title: 'Operazioni',
                icon: 'pi pi-briefcase',
                color_light: '#4DD0E1',
                color_dark: '#0097A7',
                textContent: [
                    {amount: 10, text: 'Nuove'},
                    {amount: 350, text: 'Totali'}
                ]
            }
        ];

        this.teamMembers = [
            {
                name: 'Amy Elsner',
                desc: 'Accounting',
                image: 'amyelsner'
            },
            {
                name: 'Anna Fali',
                desc: 'Procurement',
                image: 'annafali'
            },
            {
                name: 'Bernardo Dominic',
                desc: 'Finance',
                image: 'bernardodominic'
            },
            {
                name: 'Ivan Magalhaes',
                desc: 'Sales',
                image: 'ivanmagalhaes'
            },
            {
                name: 'Xuxue Feng',
                desc: 'Management',
                image: 'xuxuefeng'
            }
        ];

        this.initCharts();
    }

    initCharts() {
        const documentStyle = getComputedStyle(document.documentElement);
        const textColor = documentStyle.getPropertyValue('--text-color');
        const textColorSecondary = documentStyle.getPropertyValue('--text-color-secondary');
        const surfaceBorder = documentStyle.getPropertyValue('--surface-border');
        this.ordersChart = {
            labels: ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio'],
            datasets: [{
                label: 'Operazioni',
                data: [290000, 200000, 280000, 250000, 270000, 285000, 288000],
                backgroundColor: [
                    'rgba(100, 181, 246, 0.2)',
                ],
                borderColor: [
                    '#64B5F6',
                ],
                borderWidth: 3,
                fill: true,
                tension: .4
            }]
        };

        this.ordersChartOptions = {
            plugins: {
                legend: {
                    display: true,
                    labels: {
                        color: textColor
                    }
                }
            },
            hover: {
                mode: 'index'
            },
            scales: {
                x:{
                    ticks: {
                        color: textColorSecondary
                    },
                    grid: {
                        color:[surfaceBorder],
                        drawBorder: false
                    }
                },
                y: {
                    ticks: {
                        color: textColorSecondary,
                        min: 0,
                        max: 20
                    },
                    grid: {
                        color:[surfaceBorder],
                        drawBorder: false
                    }
                }
            }
        };

        this.revenueChart = {
            labels: ['Gate 1', 'Gate 2', 'Gate 3'],
            datasets: [{
                data: [233, 61, 106],
                backgroundColor: ['#64B5F6', '#7986CB', '#4DB6AC'],
                borderColor: [surfaceBorder]
            }]
        };

        this.revenueChartOptions = {
            plugins: {
                legend: {
                    display: true,
                    labels: {
                        color: textColor
                    }
                }
            }
        }

    }

    onGlobalFilter(table: Table, event: Event) {
        table.filterGlobal((event.target as HTMLInputElement).value, 'contains');
    }

    changeDataset(event: any) {

        // data: [290000, 200000, 280000, 250000, 270000, 285000, 288000],
        const dataSet = [
            [290000, 200000, 280000, 250000, 270000, 285000, 288000],
            [280000, 190000, 273000, 247000, 240000, 268500, 280500],
            [5000, 6000, 4000, 2000, 3000, 1500, 5000],
            [5000, 4000, 3000, 1000, 27000, 15000, 2500]
        ];

        this.ordersChart.datasets[0].data = dataSet[parseInt(event.currentTarget.getAttribute('data-index'))];
        this.ordersChart.datasets[0].label = event.currentTarget.getAttribute('data-label');
        this.ordersChart.datasets[0].borderColor = event.currentTarget.getAttribute('data-stroke');
        this.ordersChart.datasets[0].backgroundColor = event.currentTarget.getAttribute('data-fill');

    }


    ngOnDestroy() {
        //this.subscription.unsubscribe();
    }
}
