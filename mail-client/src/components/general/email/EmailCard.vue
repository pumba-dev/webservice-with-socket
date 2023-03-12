<template>
  <v-card :title="mail.subject" :text="mail.sender">
    <v-card-actions>
      <v-btn @click="$emit('openMail', mail)">Abrir</v-btn>
      <v-btn @click="$emit('replyMail', mail)">Responder</v-btn>
      <v-btn @click="$emit('forwardMail', mail)">Encaminhar</v-btn>
      <v-btn @click="$emit('deleteMail', mail)">Apagar</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
import { defineProps } from "vue";

defineProps({
  mail: {
    type: Object,
    required: true,
  },
});
</script>

<style></style>
