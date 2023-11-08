<template>
  <div>
    {{ myMsg }}
    <ParentGrandChildVue :my-msg="myMsg" />
  </div>
</template>

<script setup>
import ParentGrandChildVue from "./ParentGrandChild.vue"
// defineProps(['myMsg'])
const test = defineProps({
  myMsg : String,
  // myMsg : {
  //   type : String,
  //   required : true,
  // }
})
console.log(test.myMsg)
</script>

<style scoped>

</style>