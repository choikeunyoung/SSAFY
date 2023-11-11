<template>
  <div>
    <p class="dogdetail__p"><strong>이름 : </strong>{{  test.name }}</p>
  </div>
  <div>
    <p class="dogdetail__p"><strong>품종 : </strong>{{  test.breed_group }}</p>
  </div>
  <div>
    <p class="dogdetail__p"><strong>높이 : </strong>{{  test.height.imperial }}</p>
  </div>
  <div>
    <p class="dogdetail__p"><strong>수명 : </strong>{{  test.life_span }}</p>
  </div>
  <div>
    <p class="dogdetail__p"><strong>성격 : </strong>{{  test.temperament }}</p>
  </div>
  <div>
    <p class="dogdetail__p"><strong>무게 : </strong>{{  test.weight.imperial }}</p>
  </div>
</template>

<script setup>
defineProps({
  test : String,
})
</script>

<style scoped>

.dogdetail__p {
  margin: 0;
  padding-left: 1rem;
}
</style>