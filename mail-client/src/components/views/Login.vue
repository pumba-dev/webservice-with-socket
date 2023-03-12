<template>
  <MainCard>
    <CardHeader
      title="Login"
      subtitle="Bem-vindo de volta! Por favor insira seu nome."
    ></CardHeader>

    <CardForm>
      <InputLabel fontWeight="bold">Nome</InputLabel>
      <TextInput
        :error="v$.name.$error"
        v-model.trim="loginFieldsData.name"
        placeholder="Digite o seu nome"
      ></TextInput>

      <BlockButton
        :loading="loginIsLoading"
        :disabled="loginIsLoading"
        @click.prevent="submitLogin"
        >Entrar</BlockButton
      >
    </CardForm>
  </MainCard>
</template>

<script setup>
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import useVuelidate from "@vuelidate/core";
import { reactive, ref, computed } from "vue";
import { required } from "@vuelidate/validators";
import MainCard from "@/components/general/main-card/MainCard.vue";
import CardForm from "@/components/general/main-card/CardForm.vue";
import CardHeader from "@/components/general/main-card/CardHeader.vue";
import BlockButton from "@/components/general/buttons/BlockButton.vue";
import TextInput from "@/components/general/forms/TextInput.vue";
import InputLabel from "@/components/general/forms/InputLabel.vue";
import authentication from "@/services/authentication";

const loginFieldsData = reactive({
  name: "",
});

const store = useStore();
const router = useRouter();
const loginIsLoading = ref(false);

const loginRules = computed(() => ({
  name: {
    required,
  },
}));

const v$ = useVuelidate(loginRules, loginFieldsData);

async function submitLogin() {
  loginIsLoading.value = true;

  const formIsValid = await v$.value.$validate();

  if (formIsValid) {
    console.log("User Name: ", loginFieldsData.name);
    authentication.login(loginFieldsData.name);
    router.push("/dashboard");
  } else {
    store.dispatch("notifySystem/create", {
      type: "left",
      text: "Verifique os dados inseridos e tente novamente.",
      iconSrc: "error-icon",
    });
  }

  loginIsLoading.value = false;
}
</script>

<style></style>
