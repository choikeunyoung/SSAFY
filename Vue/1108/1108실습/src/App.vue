<script setup>
import DogList from './components/DogList.vue';
import axios from "axios"
import { ref } from 'vue';

const dogs = ref([])
// async : 이 함수가 비동기 함수다 알려주는 키워드
// await : 비동기 함수의 종료를 기다려주는 키워드
// try-catch 와 함께 자주 사용된다.

const getDogData = async () => {
  const URL = "https://api.thedogapi.com/v1/images/search?limit=10"

  try {
    const response = await axios.get(URL)
    
    const dogData = response.data
    // 비동기 쓸 때 forEach 쓰지 말자 => 순서 보장이 힘듬
    // map 안에 async 사용 시 자동 Promise 객체 반환
    const details = dogData.map(async (dog) => {
      const detailURL = `https://api.thedogapi.com/v1/images/${dog.id}`
      const detailres = await axios.get(detailURL)
      dog.detail = detailres.data.breeds ? detailres.data.breeds[0] : null
    })
    // Promise 객체 10개가 출력됨
    // promise 실행 자체는 성공했는데,
    // 순서는 보장하지 못함

    // Promise.all : Promise 배열 계산이 모두 끝날때까지 기다려줌
    await Promise.all(details)
    dogs.value = dogData
  } catch (error) {
    console.error("강아지 데이터 못불러옴", error)
  }

  // 비동기 버그 해결 코드



  // 비동기 버그 코드
  // axios.get(URL)
  // .then((res) => {
  //   const dogData = res.data
  //   dogs.value = dogData;
  //   dogData.forEach((dog) => {
  //     const detailURL = `https://api.thedogapi.com/v1/images/${dog.id}`
  //     axios.get(detailURL)
  //     .then((res) => {
  //       console.log(res.data.breeds)
  //       dog.detail = res.data
  //     })
  //     .catch((error) => {
  //       console.log(error)
  //     })
  //   })
  //   console.log("check = ", dogsDetail.value)
  // })
  // .catch((error) => {
  //   console.log(error)
  // })
}

</script>

<template>
  <div class="container">
    <h1>2023-11-08 실습</h1>
    <!-- emit 이벤트 -->
    <!-- template -> kabeb case -->
    <DogList :dogs="dogs" @get-dog-data="getDogData"/>
  </div>
</template>

<style scoped>
  .container {
    width: 80%;
    margin: 0 auto;
  }
</style>
