<template>
  <v-select
    required
    hide-details
    :error="error"
    :items="items"
    color="primary"
    density="compact"
    variant="outlined"
    :placeholder="placeholder"
  ></v-select>
</template>

<script setup>
import { defineProps } from "vue";

defineProps({
  placeholder: {
    type: String,
    required: true,
  },
  items: {
    type: Array,
    required: true,
  },
  error: {
    type: Boolean,
    required: true,
  },
});
</script>

<style scoped></style>
