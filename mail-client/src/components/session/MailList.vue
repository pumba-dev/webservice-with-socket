<template>
  <v-list>
    <v-list-item
      :key="index"
      style="cursor: pointer"
      v-for="(item, index) in mailList"
    >
      <EmailCard :title="item.subject" :preview="item.content"></EmailCard>
    </v-list-item>
  </v-list>
</template>

<script setup>
import { ref } from "vue";
import EmailCard from "@/components/general/email/EmailCard.vue";

const mailList = ref([
  {
    sender: "Remetente 01",
    receiver: "Destinatário 03",
    subject: "Título 02",
    content: "Aqui está escrito o texto...",
  },
  {
    sender: "Remetente 01",
    receiver: "Destinatário 03",
    subject: "Título 01",
    content: "Aqui está escrito o texto...",
  },
]);
</script>

<style></style>
