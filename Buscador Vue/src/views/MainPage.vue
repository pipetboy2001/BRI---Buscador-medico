<template>
  <div class="main">
  <div class="container">
    <h1 class="text-center mt-5">BUSCADOR MÉDICO</h1>
    <div class="row justify-content-center mt-5">
      <div class="col-lg-6 col-md-8 col-sm-10">
        <div class="autocomplete">
          <div class="input-group mb-3">
            <input
              class="form-control"
              type="text"
              name="searchQuery"
              v-model="searchQuery"
              placeholder="Ingresa tu consulta de búsqueda"
              autocomplete="off"
              style="width: 100%; font-size: 18px"
              @keyup.enter="redirectToSearchPage"
              @input="autocomplete"
              
            />
            <button class="btn btn-primary" @click="redirectToSearchPage">Buscar</button>
          </div>
          <div v-for="suggestion in suggestions" :key="suggestion" @click="selectSuggestion(suggestion)" style="background: #eeee; cursor:pointer">
            {{ suggestion }}
          </div>
        </div>
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
      suggestions: [],
      words: ["Obsessive",
  "Ischemic",
  "Kawasaki",
  "Anemia",
  "Gastritis",
  "Cholera",
  "Epilepsy",
  "Varicella",
  "Conjunctivitis",
  "Gout",
  "Sinusitis",
  "Bipolar",
  "Temporomandibular",
  "Esclerodermia",
  "Stress",
  "Liver",
  "Dengue",
  "Hepatitis",
  "Pneumothorax",
  "Migraine",
  "Hepatocellular",
  "Malaria",
  "Otitis",
  "Rabies",
  "Pneumococcal",
  "HIV",
  "Bubonic",
  "Tetanus",
  "Eating",
  "Alzheimer",
  "Rubella",
  "Schizophrenia",
  "Diabetes",
  "Cardiovascular",
  "Sleep",
  "Tuberculosis",
  "Lung",
  "Patellar",
  "Cirrhosis",
  "Tonsillitis",
  "Torticollis",
  "Ebola",
  "Parkinson"]
    };
  },
  methods: {
    redirectToSearchPage() {
      if (this.searchQuery) {
        const encodedQuery = encodeURIComponent(this.searchQuery);
        console.log('Consulta de búsqueda:', encodedQuery);
        
        this.$router.push({
          name: 'BusquedaPage',
          query: {
            q: encodedQuery,
          },
        });
      }
    },
    selectSuggestion(suggestion) {
      this.searchQuery = suggestion;
      this.redirectToSearchPage();
    },
    autocomplete() {
      this.suggestions = this.words.filter(word => word.toLowerCase().startsWith(this.searchQuery.toLowerCase())).slice(0, 4);
      console.log(this.suggestions);
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
  font-family: 'Roboto', sans-serif;
  color: #ebeef3;
  font-size: 50px;
  font-weight: 700;
  letter-spacing: 1px;
  text-shadow: 0 0 10px #000;
  -webkit-text-stroke: 2px #000;
}

.form-control {
  font-size: 17px;
}

.btn-primary {
  font-size: 17px;
}
.autocomplete-dropdown {
  background-color: white;
  border: 1px solid #ccc;
  list-style-type: none;
  margin: 0;
  padding: 0;
  position: absolute;
  width: 100%;
  z-index: 100;
  box-sizing: border-box;
  max-height: 200px; /* Adjust this value according to your desired max height */
  overflow-y: auto;
}
.autocomplete {
  position: relative;
  width: 100%;
}
/* Color de fondo de la vista */
body {
  background-color: #ebeef3;
}

.main {
    background-image:url("../assets/ADN roche.jpg");
    width:100%;			
    height:100%;			
    position:fixed;
    background-size:100% 100%;
    /*filter: blur(5px);*/
}

</style>
