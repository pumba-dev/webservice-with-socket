<template>
  <!-- Left Notify -->
  <v-list
    lines="two"
    class="bg-transparent ma-5"
    style="position: absolute; z-index: 3000; bottom: 0; left: 0"
  >
    <NotifyCard
      :key="index"
      v-for="(notify, index) in leftNotifyList"
      :text="notify.text"
      :iconSrc="notify.iconSrc"
      :icon="notify.icon"
      @closeNotify="removeNotify(index)"
    ></NotifyCard>
  </v-list>

  <!-- Right Notify -->
  <v-list
    lines="two"
    class="bg-transparent ma-5"
    style="position: absolute; z-index: 3000; top: 0; right: 0"
  >
    <NotifyCard
      :key="index"
      v-for="(notify, index) in rightNotifyList"
      :text="notify.text"
      :iconSrc="notify.iconSrc"
      :icon="notify.icon"
      :color="notify.color"
      @closeNotify="removeNotify(index)"
    ></NotifyCard>
  </v-list>
</template>

<script setup>
import { computed } from "vue";
import { useStore } from "vuex";
import NotifyCard from "@/components/general/notify-system/NotifyCard.vue";

const store = useStore();

const leftNotifyList = computed(() => {
  const notifyList = store.getters["notifySystem/getAll"];
  return notifyList.filter((notify) => notify.type == "left");
});

const rightNotifyList = computed(() => {
  const notifyList = store.getters["notifySystem/getAll"];
  return notifyList.filter((notify) => notify.type == "right");
});

function removeNotify(index) {
  store.dispatch("notifySystem/remove", index);
}
</script>

<style></style>
