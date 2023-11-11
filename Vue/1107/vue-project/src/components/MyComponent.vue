<template>
  <div class="greeting">
    <MyComponentItemVue />
  </div>
</template>

<script setup>
import { ref } from "vue"
import MyComponentItemVue from "./MyComponentItem.vue"


const msg = ref("hello world")
</script>

<style scoped>
.greeting {
  color:red;
}
</style>