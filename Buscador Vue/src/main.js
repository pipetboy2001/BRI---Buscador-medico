import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import SearchPage from './views/SearchPage.vue';
import App from './App.vue';
import { Client } from 'elasticsearch-browser';

const client = new Client({
    node: 'http://localhost:9200', // Reemplaza con la URL de tu servidor Elasticsearch
});

const routes = [
    {
        path: '/',
        component: SearchPage,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

createApp(App).use(router).mount('#app');
