<template>
  <div>
    <h1 class="text-center mt-5">Resultados de búsqueda</h1>
    <div class="row justify-content-center mt-5">
      <div class="col-lg-6 col-md-8 col-sm-10">
        <input type="text" v-model="query" class="form-control" placeholder="Ingresa tu consulta de búsqueda" />
        <button @click="search" class="btn btn-primary mt-3">Buscar</button>
        <div v-if="results.length === 0 && searchCompleted" class="mt-3">No se encontraron resultados.</div>
        <div v-else>
          <div v-for="result in results" :key="result._id" @click="viewResult(result)" class="result-card">
            <h3>{{ result._source.nombre }}</h3>
            <p>Revista: {{ result._source.revista }}</p>
            <p>Autor/es: {{ result._source.autores }}</p>
            <p>Año: {{ result._source.anio }}</p>
            <p>Keywords: {{ result._source.keywords }}</p>
            <p>Idioma: {{ result._source.idioma }}</p>
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
      results: [], // Los resultados de la búsqueda
      searchCompleted: false, // Indica si la búsqueda se ha completado
      activeId: null // ID del resultado activo en el acordeón
    };
  },

  methods: {
    toggleAccordion(id) {
      if (this.activeId === id) {
        this.activeId = null; // Si se hace clic en el resultado activo, se cierra el acordeón
      } else {
        this.activeId = id; // Se establece el nuevo resultado activo
      }
    },
    search() {
      this.results = [];
      this.searchCompleted = false;

      axios
        // Editar según la dirección de su servidor Elasticsearch
        .get('http://localhost:9200/buscador/_search', {
          params: {
            q: `contenido:"${this.query}"` // Búsqueda por el término ingresado en el campo de búsqueda
          }
        })
        .then(response => {
          const hits = response.data.hits.hits;
          this.results = hits;
          this.searchCompleted = true;
        })
        .catch(error => {
          console.error(error);
          this.results = [];
          this.searchCompleted = true;
        });
    }
  }
};
</script>

<style scoped>
.text-center {
  text-align: center;
}

.mt-5 {
  margin-top: 5rem;
}

.mt-3 {
  margin-top: 3rem;
}

.result-card {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
  cursor: pointer;
}

.result-card h3 {
  font-size: 18px;
  margin-bottom: 5px;
}

.result-card p {
  font-size: 14px;
  margin-bottom: 3px;
}