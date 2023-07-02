<template>
    <div class="navegador">
        <input class="texto" type="text" placeholder="Ingresa tu consulta de búsqueda" />
        <button class="boton" @click="search">Buscar</button>
    </div>
  </template>
  
  <script>
  export default {
    components: {
    },
  };
  </script>
<style> /* Style global de la mainpage*/
    body {
        justify-content: center;
        align-items: center;
    }
</style>
<style scoped> /* Style scoped de la mainpage*/
    .navegador{
        padding-top: 25%;
        position: relative;
    }
    .texto{
        font-size: 17px;
        outline: none;
        border: none;
    }
    .boton{
        float: right;
        padding: 6px;
        background: #ddd;
        font-size: 17px;
        border: none;
        cursor: pointer;
    }
</style>

  