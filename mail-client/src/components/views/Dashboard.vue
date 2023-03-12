<template>
  <v-app id="inspire">
    <NavigationDrawer
      @openSendMail="selectedMenu = 'send-mail'"
      @openMailList="selectedMenu = 'mail-list'"
    ></NavigationDrawer>

    <v-app-bar>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Lista de E-mails</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <component :is="sessionComponent"></component>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref, computed } from "vue";
import NavigationDrawer from "@/components/general/navigation/NavigationDrawer";
import MailList from "@/components/session/MailList";
import SendMail from "@/components/session/SendMail";

const selectedMenu = ref("mail-list");
const sessionComponent = computed(() => {
  switch (selectedMenu.value) {
    case "mail-list":
      return MailList;
    case "send-mail":
      return SendMail;
    default:
      return null;
  }
});
</script>

<style></style>
