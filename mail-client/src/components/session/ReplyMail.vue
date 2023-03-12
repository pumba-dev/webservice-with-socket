<template>
  <v-card>
    <v-card-title class="d-flex justify-space-between align-center my-2">
      <span class="text-subtitle-1 font-weight-bold">Responder E-mail</span>
    </v-card-title>

    <v-divider></v-divider>

    <v-sheet class="pa-5">
      <v-row class="flex justify-center">
        <v-col>
          <InputLabel>Destinatário</InputLabel>

          <TextInput
            disabled
            v-model="fieldsData.receiver"
            :error="v$.receiver.$error"
            placeholder="Digite o destinatário"
          ></TextInput>
        </v-col>

        <v-col>
          <InputLabel>Assunto</InputLabel>

          <TextInput
            disabled
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
        class="mx-2"
        :loading="replyIsLoading"
        :disabled="replyIsLoading"
        @click.prevent="$emit('openMailList')"
      >
        Voltar
      </DashboardButton>
      <DashboardButton
        :loading="replyIsLoading"
        :disabled="replyIsLoading"
        @click.prevent="replyMail"
      >
        Responder
      </DashboardButton>
    </v-sheet>
  </v-card>
</template>

<script setup>
import { useStore } from "vuex";
import useVuelidate from "@vuelidate/core";
import { reactive, ref, defineEmits, defineProps, onMounted } from "vue";
import { required } from "@vuelidate/validators";
import mailService from "@/services/mail";

import InputLabel from "@/components/general/forms/InputLabel.vue";
import TextInput from "@/components/general/forms/TextInput.vue";
import TextAreaInput from "@/components/general/forms/TextAreaInput.vue";
import DashboardButton from "@/components/general/buttons/DashboardButton.vue";

const replyIsLoading = ref(false);
const store = useStore();

onMounted(() => {
  fieldsData.receiver = props.email.sender;
  fieldsData.subject = "RE: " + props.email.subject;
  fieldsData.content =
    "\n" +
    "-----------------------------------------------------------------\n" +
    props.email.content;
});

const emit = defineEmits("openMailList");

const props = defineProps({
  email: {
    type: Object,
    required: true,
  },
});
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

async function replyMail() {
  replyIsLoading.value = true;

  const formIsValid = await v$.value.$validate();

  if (formIsValid) {
    const emailID = props.email.id;
    console.log("Forward Data", emailID, fieldsData.content);
    await mailService
      .reply(emailID, fieldsData.content)
      .then((response) => {
        console.log("response: ", response);
        store.dispatch("notifySystem/create", {
          text: "E-mail respondido com sucesso!.",
          icon: "mdi-check-circle-outline",
          color: "sucess",
        });
        emit("openMailList");
      })
      .catch((error) => {
        console.log("error: ", error);
        store.dispatch("notifySystem/create", {
          text: "Erro interno ao responder e-mail.",
          icon: "mdi-alert-circle-outline",
          color: "error",
        });
      });
    replyIsLoading.value = false;
  } else {
    store.dispatch("notifySystem/create", {
      text: "Verifique os dados inseridos e tente novamente.",
      icon: "mdi-alert-circle-outline",
      color: "error",
    });
    replyIsLoading.value = false;
  }
}
</script>

<style></style>
