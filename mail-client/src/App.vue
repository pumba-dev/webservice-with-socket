<template>
  <v-app>
    <router-view />
    <NotifySystem></NotifySystem>
  </v-app>
</template>

<script setup>
import NotifySystem from "@/components/general/notify-system/NotifySystem.vue";
</script>
