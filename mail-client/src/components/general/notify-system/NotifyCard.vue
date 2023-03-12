<template>
  <v-card
    width="500"
    class="elevation-1 bg-surface my-2 d-flex px-4 py-3 d-flex align-center"
  >
    <!-- Icon or SVG Image -->
    <v-icon
      v-if="!iconSrc"
      :color="color"
      max-width="35"
      min-width="35"
      size="large"
      >{{ icon }}</v-icon
    >

    <v-img
      v-if="iconSrc"
      max-width="35"
      min-width="35"
      src="@/assets/icons/${iconSrc}.svg"
    />

    <!-- Text -->
    <span
      class="pl-6 text-primary-text overflow-hidden text-wrap ellipsis-one-line"
      >{{ text }}</span
    >

    <!-- Close Button -->
    <v-icon
      size="small"
      color="secondary-text"
      class="ml-auto"
      icon="mdi-close"
      @click="$emit('closeNotify')"
    ></v-icon>
  </v-card>
</template>

<script setup>
import { defineProps } from "vue";

defineProps({
  text: {
    type: String,
    required: true,
  },
  iconSrc: String,
  icon: {
    type: String,
    default: "mdi-alert-circle",
  },
  color: {
    type: String,
    default: "primary",
  },
});
</script>

<style></style>
