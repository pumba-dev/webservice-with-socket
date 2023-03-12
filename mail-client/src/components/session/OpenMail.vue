<template>
  <v-card>
    <v-card-title class="d-flex justify-space-between align-center my-2">
      <span class="text-subtitle-1 font-weight-bold">Visualizar E-mail</span>
    </v-card-title>

    <v-divider></v-divider>

    <v-sheet class="pa-5">
      <v-row class="flex justify-center">
        <v-col>
          <InputLabel>Remetente</InputLabel>

          <TextInput
            disabled
            v-model="fieldsData.sender"
            placeholder="Digite o destinatário"
          ></TextInput>
        </v-col>

        <v-col>
          <InputLabel>Assunto</InputLabel>

          <TextInput
            disabled
            v-model="fieldsData.subject"
            placeholder="Digite o assunto"
          ></TextInput>
        </v-col>
      </v-row>

      <v-row class="">
        <v-col>
          <InputLabel>Mensagem</InputLabel>

          <TextAreaInput
            readonly
            class="h-100"
            v-model="fieldsData.content"
            placeholder="Digite a mensagem do e-mail"
          ></TextAreaInput>
        </v-col>
      </v-row>
    </v-sheet>

    <v-divider></v-divider>

    <v-sheet class="d-flex justify-end py-4 px-6">
      <DashboardButton class="mx-2" @click.prevent="$emit('openMailList')">
        Voltar
      </DashboardButton>
      <DashboardButton class="mx-2" @click.prevent="$emit('replyMail', email)">
        Responder
      </DashboardButton>
      <DashboardButton
        class="mx-2"
        @click.prevent="$emit('forwardMail', email)"
      >
        Encaminhar
      </DashboardButton>
    </v-sheet>
  </v-card>
</template>

<script setup>
import { reactive, defineEmits, defineProps, onMounted } from "vue";

import InputLabel from "@/components/general/forms/InputLabel.vue";
import TextInput from "@/components/general/forms/TextInput.vue";
import TextAreaInput from "@/components/general/forms/TextAreaInput.vue";
import DashboardButton from "@/components/general/buttons/DashboardButton.vue";

onMounted(() => {
  fieldsData.sender = props.email.sender;
  fieldsData.subject = props.email.subject;
  fieldsData.content = props.email.content;
});

defineEmits("openMailList");

const props = defineProps({
  email: {
    type: Object,
    required: true,
  },
});

const fieldsData = reactive({
  sender: "",
  subject: "",
  content: "",
});
</script>

<style></style>
