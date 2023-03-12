<template>
  <v-navigation-drawer v-model="drawer">
    <h1 class="text-h5 font-weight-bold align-self-start mb-2 pa-4">
      Serviço de E-mail
    </h1>

    <v-list>
      <v-list-item
        :key="index"
        style="cursor: pointer"
        @click.prevent="handleAction(item.key)"
        v-for="(item, index) in settingOptions"
      >
        <v-list-item-title>{{ item.title }}</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script setup>
import authentication from "@/services/authentication";
import { ref, defineEmits } from "vue";
import { useRouter } from "vue-router";

const emit = defineEmits(["openSendMail", "openMailList"]);

const router = useRouter();
const drawer = ref(null);
const settingOptions = ref([
  { key: "mail-list", title: "Lista de e-mails" },
  { key: "send-mail", title: "Enviar e-mail" },
  { key: "sign-out", title: "Sair" },
]);

function handleAction(key) {
  console.log("handleAction", key);
  switch (key) {
    case "mail-list":
      emit("openMailList");
      break;
    case "send-mail":
      emit("openSendMail");
      break;
    case "sign-out":
      authentication.logout();
      router.push("/");
      break;
  }
}
</script>

<style></style>
