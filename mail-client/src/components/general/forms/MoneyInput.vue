<template>
  <v-text-field
    ref="inputRef"
    required
    hide-details
    variant="outlined"
    :error="error"
    :placeholder="placeholder"
    density="compact"
  ></v-text-field>
</template>

<script setup>
import { defineProps, watch } from "vue";
import { useCurrencyInput } from "vue-currency-input";

const props = defineProps({
  error: {
    type: Boolean,
    required: true,
  },
  placeholder: {
    type: String,
    required: true,
  },
  modelValue: Number,
});

const { inputRef, setValue } = useCurrencyInput({
  currency: "BRL",
});

watch(
  () => props.modelValue,
  (value) => {
    setValue(value);
  }
);
</script>

<style></style>
