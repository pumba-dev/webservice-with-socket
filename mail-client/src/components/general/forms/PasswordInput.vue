<template>
  <v-text-field
    required
    variant="outlined"
    :error="error"
    :placeholder="placeholder"
    :type="showPasswordField ? 'text' : 'password'"
    @click:append-inner="showPasswordField = !showPasswordField"
    :append-inner-icon="
      showPasswordField ? 'mdi-eye-outline' : 'mdi-eye-off-outline'
    "
    density="compact"
  ></v-text-field>
</template>

<script setup>
import { defineProps, ref } from "vue";
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

const showPasswordField = ref(false);
</script>

<style></style>
