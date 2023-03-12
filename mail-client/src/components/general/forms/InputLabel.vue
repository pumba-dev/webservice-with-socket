<template>
  <p :class="`font-weight-${fontWeight} text-${fontSize} text-secondary mb-2`">
    <slot></slot>
  </p>
</template>

<script setup>
import { defineProps } from "vue";
defineProps({
  fontWeight: {
    type: String,
    default: "medium",
  },
  fontSize: {
    type: String,
    default: "text-caption",
  },
});
</script>

<style></style>
