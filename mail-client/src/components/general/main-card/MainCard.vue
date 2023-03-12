<template>
  <v-main
    class="d-flex flex-row align-center justify-center h-screen bg-background"
  >
    <v-card
      class="elevation-2 d-flex flex-column rounded-xl pa-15 align-center justify-start bg-surface"
      min-width="535"
      max-width="535"
      min-height="630"
      max-height="630"
    >
      <slot></slot>
    </v-card>
  </v-main>
</template>

<script></script>
