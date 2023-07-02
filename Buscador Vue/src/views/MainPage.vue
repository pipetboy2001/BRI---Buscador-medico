<template>
  <div class="container">
    <h1 class="text-center mt-5">BUSCADOR MÉDICO</h1>
    <div class="row justify-content-center mt-5">
      <div class="col-lg-6 col-md-8 col-sm-10">
        <div class="input-group mb-3">
          <input class="form-control" type="text" v-model="searchQuery" placeholder="Ingresa tu consulta de búsqueda" />
          <button class="btn btn-primary" @click="redirectToSearchPage">Buscar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '',
    };
  },
  methods: {
    redirectToSearchPage() {
      if (this.searchQuery) {
        this.$router.push(`/busqueda?q=${encodeURIComponent(this.searchQuery)}`);
      }
    },
  },
};
</script>

<style scoped>
.container {
  justify-content: center;
  align-items: center;
}

.mt-5 {
  margin-top: 5rem;
}

.mt-5,
.mt-5 > *,
.row.justify-content-center .col-lg-6,
.row.justify-content-center .col-md-8,
.row.justify-content-center .col-sm-10 {
  margin-top: 5rem !important;
}

.text-center {
  text-align: center;
}

.form-control {
  font-size: 17px;
}

.btn-primary {
  font-size: 17px;
}
</style>
