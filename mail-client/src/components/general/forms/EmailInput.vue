<template>
  <v-text-field
    required
    variant="outlined"
    :error="error"
    :placeholder="placeholder"
    density="compact"
  ></v-text-field>
</template>

<script setup>
import { defineProps } from "vue";
defineProps({
  error: {
    type: Boolean,
    required: true,
  },
  placeholder: {
    type: String,
    required: true,
  },
});
</script>

<style></style>
