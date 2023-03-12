<template>
  <v-app id="inspire">
    <NavigationDrawer
      @openSendMail="selectedMenu = 'send-mail'"
      @openMailList="selectedMenu = 'mail-list'"
    ></NavigationDrawer>

    <v-app-bar>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Lista de E-mails - {{ user }}</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <component
        @openMailList="selectedMenu = 'mail-list'"
        @openMail="openMail($event)"
        @replyMail="replyMail($event)"
        @forwardMail="forwardMail($event)"
        @deleteMail="deleteMail($event)"
        :email="menuItem"
        :is="sessionComponent"
      ></component>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref, computed } from "vue";
import NavigationDrawer from "@/components/general/navigation/NavigationDrawer";
import MailList from "@/components/session/MailList";
import SendMail from "@/components/session/SendMail";
import localStorage from "@/utils/localStorage";
import ForwardMail from "@/components/session/ForwardMail.vue";
import ReplyMail from "@/components/session/ReplyMail.vue";
import mailService from "@/services/mail";
import { useStore } from "vuex";

const store = useStore();
const user = ref(localStorage.get("userToken"));
const selectedMenu = ref("mail-list");
const menuItem = ref({});
const sessionComponent = computed(() => {
  switch (selectedMenu.value) {
    case "mail-list":
      return MailList;
    case "send-mail":
      return SendMail;
    case "forward-mail":
      return ForwardMail;
    case "reply-mail":
      return ReplyMail;
    default:
      return null;
  }
});

function openMail(mail) {
  console.log("Open Mail", mail);
}
function replyMail(mail) {
  console.log("Reply Mail", mail);
  menuItem.value = mail;
  selectedMenu.value = "reply-mail";
}
function forwardMail(mail) {
  console.log("Forward Mail", mail);
  menuItem.value = mail;
  selectedMenu.value = "forward-mail";
}
function deleteMail(mail) {
  console.log("Delete Mail", mail);
  mailService
    .delete(mail.id)
    .then((response) => {
      console.log("response: ", response);
      store.dispatch("notifySystem/create", {
        text: "E-mail apagado com sucesso!.",
        icon: "mdi-check-circle-outline",
        color: "sucess",
      });
      window.location.reload();
    })
    .catch((error) => {
      console.log("error: ", error);
      store.dispatch("notifySystem/create", {
        text: "Erro interno ao apagar e-mail.",
        icon: "mdi-alert-circle-outline",
        color: "error",
      });
    });
}
</script>

<style></style>
