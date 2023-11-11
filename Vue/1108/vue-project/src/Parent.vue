<template>
  <div>
    <ParentChild my-msg="Hello" :dynamic-props="name"/>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import ParentChild from './ParentChild.vue';

const name = ref("Alice")
</script>

<style scoped>

</style>