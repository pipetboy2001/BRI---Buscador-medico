import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import App from './App.vue';
import { Client } from 'elasticsearch-browser';
import 'mdb-vue-ui-kit/css/mdb.min.css';

import MainPage from './views/MainPage.vue';
import BusquedaPage from './views/BusquedaPage.vue'


const client = new Client({
    node: 'http://localhost:9200', // Reemplaza con la URL de tu servidor Elasticsearch
});

const routes = [
    {
        path: '/',
        component: MainPage,
    },
    {
        path: '/busqueda',
        name: 'BusquedaPage',
        component: BusquedaPage,
        props: (route) => ({ initialQuery: route.query.q }),
    },

];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

createApp(App).use(router).mount('#app');
