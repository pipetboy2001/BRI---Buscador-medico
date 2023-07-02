<template>
  <div>
    <input type="text" v-model="query" placeholder="Ingresa tu consulta de búsqueda" />
    <button @click="search">Buscar</button>
    <div v-if="results.length === 0 && searchCompleted">No se encontraron resultados.</div>
    <div v-else>
      <div v-for="result in results" :key="result._id">
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button class="accordion-button" type="button" @click="toggleAccordion(result._id)">
              <h3>{{ result._source.nombre }}</h3>
            </button>
          </h2>
          <div :id="'collapse-' + result._id" class="accordion-collapse collapse"
            :class="{ 'show': activeId === result._id }">
            <div class="accordion-body">
              <p>{{ result._source.contenido }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      query: '',
      results: [],  // Los resultados de la búsqueda
      searchCompleted: false,  // Indica si la búsqueda se ha completado
      activeId: null  // ID del resultado activo en el acordeón
    };
  },

  methods: {
    toggleAccordion(id) {
      if (this.activeId === id) {
        this.activeId = null;  // Si se hace clic en el resultado activo, se cierra el acordeón
      } else {
        this.activeId = id;  // Se establece el nuevo resultado activo
      }
    },
    search() {
      this.results = [];
      this.searchCompleted = false;

      axios
        // editar según la dirección de su servidor Elasticsearch
        .get('http://localhost:9200/buscador/_search', {
          params: {
            q: `contenido:"${this.query}"`, // Búsqueda por el término ingresado en el campo de búsqueda
          },
        })
        .then((response) => {
          const hits = response.data.hits.hits;
          this.results = hits;
          this.searchCompleted = true;
        })
        .catch((error) => {
          console.error(error);
          this.results = [];
          this.searchCompleted = true;
        });
    },
  },
};
</script>


