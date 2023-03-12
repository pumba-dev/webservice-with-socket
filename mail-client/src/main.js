import "@/styles/reset.css";
import "@/styles/global.css";
import store from "@/store";
import router from "@/router";
import { createApp } from "vue";
import App from "@/App.vue";
import vuetify from "@/plugins/vuetify";

createApp(App).use(store).use(router).use(vuetify).mount("#app");
