<template>
  <div>
    <search-form @search="performSearch" />
    <search-result :results="searchResults" />
  </div>
</template>

<script>

import SearchForm from "../components/SearchForm.vue";
import SearchResult from "../components/SearchResult.vue";

export default {
  components: {
    SearchForm,
    SearchResult,
  },
  data() {
    return {
      searchResults: [],
    };
  },
  methods: {
    performSearch(query) {
      // Aquí puedes enviar la consulta de búsqueda al backend y actualizar los resultados
      // Utiliza Vuex para manejar el estado si es necesario
      // Puedes utilizar la biblioteca axios para enviar solicitudes HTTP al backend
    },
  },
};
</script>
