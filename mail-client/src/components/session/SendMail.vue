<template>
  <v-card>
    <v-card-title class="d-flex justify-space-between align-center my-2">
      <span class="text-subtitle-1 font-weight-bold">Enviar E-mail</span>
    </v-card-title>

    <v-divider></v-divider>

    <v-sheet class="pa-5">
      <v-row class="flex justify-center">
        <v-col>
          <InputLabel>Destinatário</InputLabel>

          <TextInput
            v-model="fieldsData.receiver"
            :error="v$.receiver.$error"
            placeholder="Digite o destinatário"
          ></TextInput>
        </v-col>

        <v-col>
          <InputLabel>Assunto</InputLabel>

          <TextInput
            v-model="fieldsData.subject"
            :error="v$.subject.$error"
            placeholder="Digite o assunto"
          ></TextInput>
        </v-col>
      </v-row>

      <v-row class="">
        <v-col>
          <InputLabel>Mensagem</InputLabel>
          <TextAreaInput
            class="h-100"
            v-model="fieldsData.content"
            :error="v$.content.$error"
            placeholder="Digite a mensagem do e-mail"
          ></TextAreaInput>
        </v-col>
      </v-row>
    </v-sheet>

    <v-divider></v-divider>

    <v-sheet class="d-flex justify-end py-4 px-6">
      <DashboardButton
        :loading="sendIsLoading"
        :disabled="sendIsLoading"
        @click.prevent="sendMail"
      >
        Enviar
      </DashboardButton>
    </v-sheet>
  </v-card>
</template>

<script setup>
import { useStore } from "vuex";
import useVuelidate from "@vuelidate/core";
import { reactive, ref, defineEmits } from "vue";
import { required } from "@vuelidate/validators";
import mailService from "@/services/mail";

import InputLabel from "@/components/general/forms/InputLabel.vue";
import TextInput from "@/components/general/forms/TextInput.vue";
import TextAreaInput from "@/components/general/forms/TextAreaInput.vue";
import DashboardButton from "@/components/general/buttons/DashboardButton.vue";
import localStorage from "@/utils/localStorage";

const sendIsLoading = ref(false);
const store = useStore();

const emit = defineEmits("openMailList");

const fieldsData = reactive({
  receiver: "",
  subject: "",
  content: "",
});

const rules = reactive({
  receiver: {
    required,
  },
  subject: {
    required,
  },
  content: {
    required,
  },
});

const v$ = useVuelidate(rules, fieldsData);

async function sendMail() {
  sendIsLoading.value = true;

  const formIsValid = await v$.value.$validate();

  if (formIsValid) {
    const sender = localStorage.get("userToken");
    console.log("Mensagem: ", { sender, ...fieldsData });
    await mailService
      .send(sender, fieldsData.receiver, fieldsData.subject, fieldsData.content)
      .then((response) => {
        console.log("response: ", response);
        store.dispatch("notifySystem/create", {
          text: "E-mail enviado com sucesso!.",
          icon: "mdi-check-circle-outline",
          color: "sucess",
        });
        emit("openMailList");
      })
      .catch((error) => {
        console.log("error: ", error);
        store.dispatch("notifySystem/create", {
          text: "Erro interno ao enviar e-mail.",
          icon: "mdi-alert-circle-outline",
          color: "error",
        });
      });
    sendIsLoading.value = false;
  } else {
    store.dispatch("notifySystem/create", {
      text: "Verifique os dados inseridos e tente novamente.",
      icon: "mdi-alert-circle-outline",
      color: "error",
    });
    sendIsLoading.value = false;
  }
}
</script>

<style></style>
