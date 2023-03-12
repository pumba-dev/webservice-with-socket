<template>
  <v-btn
    height="32"
    :style="{ border: buttonBorder }"
    flat
    :variant="buttonVariant"
    size="x-small"
    :color="buttonColor"
    class="rounded-sm mx-1"
  >
    <slot></slot>
  </v-btn>
</template>

<script setup>
import { defineProps, computed } from "vue";
import { useTheme } from "vuetify";

const theme = useTheme();

const props = defineProps({
  active: {
    type: Boolean,
    default: false,
  },
  background: {
    type: Boolean,
    default: true,
  },
});

const buttonVariant = computed(() => {
  if (!props.background) {
    return "text";
  } else if (props.active) {
    return "tonal";
  } else {
    return "outlined";
  }
});

const buttonColor = computed(() => {
  if (!props.background) {
    return "secondary-text";
  } else if (props.active) {
    return "primary";
  } else {
    return "secondary-text";
  }
});

const buttonBorder = computed(() => {
  if (!props.background) {
    return "none";
  } else if (props.active) {
    return `1px solid ${theme.current.value.colors.primary}`;
  } else {
    return `1px solid ${theme.current.value.colors.border}`;
  }
});
</script>

<style></style>
