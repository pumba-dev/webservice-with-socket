<template>
  <v-text-field
    required
    hide-details
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
    default: false,
  },
  placeholder: {
    type: String,
    required: true,
  },
});
</script>

<style></style>
