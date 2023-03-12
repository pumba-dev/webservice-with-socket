<template>
  <v-img width="200" class="mb-13" src="src/assets/logomarca.png" fill />

  <h1 class="text-h5 font-weight-bold align-self-start mb-2">
    {{ title }}
  </h1>
  <span class="text-subtitle-2 align-self-start mb-9">
    {{ subtitle }}
  </span>
</template>

<script setup>
import { defineProps } from "vue";

defineProps({
  title: {
    type: String,
    required: true,
  },
  subtitle: {
    type: String,
    required: true,
  },
});
</script>

<style></style>
