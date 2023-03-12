<template>
  <v-btn variant="text" :class="`text-${color} text-subtitle-1`"
    ><slot></slot
  ></v-btn>
</template>

<script setup>
import { defineProps } from "vue";
defineProps({
  color: {
    type: String,
    default: "primary",
  },
});
</script>

<style></style>
