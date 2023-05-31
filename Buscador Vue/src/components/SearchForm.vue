<template>
  <div>
    <input type="text" v-model="query" placeholder="Ingresa tu consulta de búsqueda" />
    <button @click="search">Buscar</button>

    <div v-if="results.length === 0 && searchCompleted">No se encontraron resultados.</div>
    <div v-else>
      <div v-for="result in results" :key="result._id">
        <h3>{{ result._source.nombre }}</h3>
        <p>{{ result._source.contenido }}</p>
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
      results: [],
      searchCompleted: false,
    };
  },
  methods: {
    search() {
      this.results = [];
      this.searchCompleted = false;

      axios
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
        });
    },
  },
};
</script>
