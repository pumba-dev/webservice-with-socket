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
import { ref, onMounted } from "vue";
import EmailCard from "@/components/general/email/EmailCard.vue";
import mailService from "@/services/mail";
import localStorage from "@/utils/localStorage";

onMounted(() => {
  console.log("Mail List Mounted");
  fetchMailList();
});

const mailList = ref([]);

function fetchMailList() {
  const user = localStorage.get("userToken");
  mailService
    .getByReceiver(user)
    .then((response) => {
      console.log(response);
      mailList.value = response.data.data;
    })
    .catch((error) => {
      console.log(error);
    });
}
</script>

<style></style>
