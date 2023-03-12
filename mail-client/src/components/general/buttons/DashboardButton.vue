<template>
  <v-btn
    color="primary"
    class="text-body-2 font-weight-light px-5"
    :variant="variant"
  >
    <slot></slot>
  </v-btn>
</template>

<script setup>
import { defineProps } from "vue";

defineProps({
  variant: {
    type: String,
    default: "elevated",
  },
});
</script>

<style></style>
