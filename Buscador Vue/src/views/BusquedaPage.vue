<template>
  <div>
    <h1 class="text-center mt-5">Resultados de búsqueda</h1>
    <div class="row justify-content-center mt-5">
      <div class="col-lg-6 col-md-8 col-sm-10">
        <input
          type="text"
          v-model="query"
          class="form-control"
          placeholder="Ingresa tu consulta de búsqueda"
          id="myInput"
        />
        <button @click="search" class="btn btn-primary mt-3">Buscar</button>
        <div v-if="results.length === 0 && searchCompleted" class="mt-3">
          No se encontraron resultados.
        </div>
        <div v-else>
          <div
            v-for="result in results"
            :key="result._id"
            :class="{
              'result-card': true,
              active: result._id === selectedResultId,
            }"
          >
            <span
              class="nextPage"
              style="cursor: pointer"
              @click="viewResult(result)"
            >
              <h3>{{ result._source.nombre }}</h3>
            </span>

            <p>Revista: {{ result._source.revista }}</p>
            <p>Autor/es: {{ result._source.autores }}</p>
            <p>Año: {{ result._source.año }}</p>
            <p>Keywords: {{ result._source.keywords }}</p>
            <p>Idioma: {{ result._source.idioma }}</p>
            <p>
              Abstract:
              <span v-if="result._source.abstract.length > 100">
                <span v-if="result._source.showFullAbstract">
                  {{ result._source.abstract }}
                  <button @click="toggleAbstract(result)" class="btn-show-more">
                    Mostrar menos
                  </button>
                </span>
                <span v-else>
                  {{ result._source.abstract.substring(0, 100) }}...
                  <button @click="toggleAbstract(result)" class="btn-show-more">
                    Mostrar más
                  </button>
                </span>
              </span>
              <span v-else>
                {{ result._source.abstract }}
              </span>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <MDBModal v-on:shown="setFocus" v-model="show">
  <MDBModalBody>
    <h3>Vista previa</h3>
    <iframe :src="'data:application/pdf;base64,' + selectedResult " style="width: 100%; height: 500px;"></iframe>
    <!-- Resto del contenido del modal -->
    <MDBBtn color="primary" @click="show = false">Cerrar</MDBBtn>
  </MDBModalBody>
</MDBModal>

</template>

<script>
import axios from "axios";
import { MDBModal, MDBModalBody, MDBInput, MDBBtn } from 'mdb-vue-ui-kit';
  import { ref } from 'vue'

export default {
  props: {
    initialQuery: {
      type: String,
      default: "",
    },
    showModal: {
      type: Boolean,
      default: false,
    },
  },

  components: {
      MDBModal,
      MDBModalBody,
      MDBInput,
      MDBBtn,
    },
    setup() {
      const setFocus = () => {
        const myInput = document.getElementById('myInput');
        myInput.focus();
      }
      const show = ref(false);
      return {
        setFocus,
        show,
      };
    },


  data() {
    return {
      query: "",
      results: [], // Los resultados de la búsqueda
      searchCompleted: false, // Indica si la búsqueda se ha completado
      activeId: null, // ID del resultado activo en el acordeón
      selectedResultId: null, // ID del resultado seleccionado
      modalVisible: false, // Variable local para controlar el estado del modal
      selectedResult: null,
    };
  },

  created() {
    // Realizar búsqueda automáticamente cuando se carga el componente
    if (this.initialQuery) {
      this.query = this.initialQuery;
      this.search();
    }
  },

  methods: {
    search() {
      console.log("Consulta de búsqueda:", this.query);

      this.results = [];
      this.searchCompleted = false;

      axios
        // Editar según la dirección de su servidor Elasticsearch
        .get("http://localhost:9200/buscador/_search", {
          params: {
            q: `contenido:"${this.query}"`, // Búsqueda por el término ingresado en el campo de búsqueda
          },
        })
        .then((response) => {
          const hits = response.data.hits.hits;
          // Agregar una propiedad "showFullAbstract" a cada resultado
          this.results = hits.map((hit) => {
            return {
              ...hit,
              _source: {
                ...hit._source,
                showFullAbstract: false,
              },
            };
          });
          this.searchCompleted = true;
        })
        .catch((error) => {
          console.error(error);
          this.results = [];
          this.searchCompleted = true;
        });
    },
    viewResult(result) {
      this.selectedResultId = result._id;
      this.selectedResultId = result._id;
      console.log("ID del resultado seleccionado:", this.selectedResultId);
      this.selectedResult = result._source.pdf_base64;
      console.log("Modal visible antes de cambiar a true:", this.show);
      this.show = true; // Abre el modal estableciendo la variable "show" en "true"
      console.log("Modal visible después de asignar true:", this.show);
    },
    toggleAbstract(result) {
      result._source.showFullAbstract = !result._source.showFullAbstract;
    },
    openModal() {
      console.log("HOLLAAA:", this.modalVisible);
      this.modalVisible = true;
      console.log("CHAOOOO:", this.modalVisible);
    },
    closeModal() {
      console.log("Modal visible antes de cerrar:", this.modalVisible);
      this.modalVisible = false;
      console.log("Modal visible después de cerrar:", this.modalVisible);
    },
  },
};
</script>

<style>
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
}

.result-card h3 {
  font-size: 18px;
  margin-bottom: 5px;
}

.result-card p {
  font-size: 14px;
  margin-bottom: 3px;
}

.nextPage {
  cursor: pointer;
}

.btn-show-more {
  margin-left: 5px;
}

.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  padding: 20px;
  transition: opacity 0.3s;
  opacity: 0;
}

.modal-enter-active,
.modal-leave-active {
  opacity: 1;
}

.modal-enter,
.modal-leave-to {
  opacity: 0;
}
</style>
