<template>
  <v-card :title="title" :text="preview">
    <v-card-actions>
      <v-btn>Abrir</v-btn>
      <v-btn>Responder</v-btn>
      <v-btn>Encaminhar</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
import { defineProps } from "vue";

defineProps({
  title: {
    type: String,
    required: true,
  },
  preview: {
    type: String,
    required: true,
  },
});
</script>

<style></style>
