<template>
  <v-btn
    block
    type="submit"
    :class="`text-center bg-${color} fill-height rounded h-10 pa-4 my-4 font-weight-light text-capitalize`"
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
