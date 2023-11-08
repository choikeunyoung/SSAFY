<template>
  <div class="header">
    <h1>랜덤한 강아지</h1>
    <button @click="getRandomDogData">새로운 강아지 가져오기</button>
  </div>
  
  <ul class="dogList">
    <div v-if="dogIsEmpty">
      <li v-for="dog in dogs" :key="dog.id">
        <img :src="dog.url" alt="">
        <div v-if="dog.detail">
          <DogDetailVue :test="dog.detail"/>
        </div>
        <!-- <div v-if="dog.detail">
          <div>
            <p><strong>이름 : </strong>{{  dog.detail.name }}</p>
          </div>
          <div>
            <p><strong>품종 : </strong>{{  dog.detail.breed_group }}</p>
          </div>
          <div>
            <p><strong>높이 : </strong>{{  dog.detail.height.imperial }}</p>
          </div>
          <div>
            <p><strong>수명 : </strong>{{  dog.detail.life_span }}</p>
          </div>
          <div>
            <p><strong>성격 : </strong>{{  dog.detail.temperament }}</p>
          </div>
          <div>
            <p><strong>무게 : </strong>{{  dog.detail.weight.imperial }}</p>
          </div>
        </div>
        <div v-else>
          <p>상세 정보 없음</p>
        </div> -->
      </li>
    </div>
    <div v-else>
      데이터가 없습니다
    </div>
  </ul>
</template>

<script setup>
import { computed } from "vue"
import DogDetailVue from "./DogDetail.vue"

const emit = defineEmits(['getDogData'])

const getRandomDogData = () => {
  emit("getDogData")
}

const props = defineProps({
  dogs : Array
})

const dogIsEmpty = computed(() => {
  return props.dogs.length > 0 ? true : false
})
</script>

<style scoped>
  ul, li {
    list-style: none;
  }
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .header > button {
    background-color: #6c5ce7c4;
    color: white;
    border: none;
    border-radius: .5rem;
    height: 50%;
    padding: 1rem 2rem;
    outline: none;
  }

  .header > button:hover {
    cursor: pointer;
    background-color: #6c5ce7;
  }

  .dogList {
    width: 80%;
    display: flex;
    flex-direction: column;
  }

  .dogList > div > li {
    display: flex;
    margin: 1rem 0;
    padding: 1rem 0;
  }
  /* .dogList > div > li > div {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  } */

  /* .dogList > div > li > div > div > p {
    margin: 0;
    padding-left: 1rem;
  } */
  .dogList > div > li > div {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .dogList > div > li > img {
    width: 200px;
    height: 200px;
    border-radius: 1rem;
    /* object-fit: fill; */
  }
</style>