<template>
  <div>
    <ul>
      <li v-for="result in results" :key="result._id">
        {{ result._source.nombre }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    results: {
      type: Array,
      required: true,
    },
  },
};
</script>
