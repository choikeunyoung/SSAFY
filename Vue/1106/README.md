# Vue

## Computed Properties

 - computed() : 계산된 속성을 정의하는 함수
 ```JS
  const todos = ref({
    { text: "Vue 실습"},
    { text: "자격증 공부"},
    { text: "TIL 작성"},
  })

  const { createApp, ref, computed } = Vue;

  const restOfTodos = computed(() => {
    return todos.value.length > 0 ? "아직 남았다" : "퇴근!"
  })
 ```

 - 반환되는 값은 computed ref이며 일반 refs와 유사하게 계산된 결과를 .value로 참조 할 수 있음 (템플릿에서는 .value 생략 가능)
 - computed 속성은 의존된 반응형 데이터를 자동으로 추적
 - 의존하는 데이터가 변경될 때만 재평가
   - restOfTodos의 계산은 todos에 의존하고 있음
   - todos가 변경될 때만 restOfTodos가 업데이트 됨

### computed와 동일한 로직을 처리할 수 있는 method

 - computed 속성 대신 method로 동일한 기능을 정의할 수 있음
 - 두 가지 접근 방식은 실제로 완전히 동일

### computed와 method 차이

 - computed 속성은 의존된 반응형 데이터를 기반으로 캐시(cached)된다.
 - 의존하는 데이터가 변경된 경우에만 재평가됨
 - 의존된 반응형 데이터가 변경되지 않는 한 이미 계산된 결과에 대한 여러 참조는 다시 평가할 필요 없이 이전에 계산된 결과를 즉시 반환
 - 다시 렌더링 발생할 때마다 항상 함수를 실행

### computed와 method의 적절한 사용처

 - computed
   - 의존하는 데이터에 따라 결과가 바뀌는 계산된 속성을 만들 때 유용
   - 동일한 의존성을 가진 여러 곳에서 사용할 때 계산 결과를 캐싱하여 중복 계산 방지

 - method
   - 단순히 특정 동작을 수행하는 함수를 정의할 때 사용
   - 데이터에 의존하는지 여부와 관계없이 항상 동일한 결과를 반환하는 함수

### method와 computed 정리

 - computed : 의존된 데이터가 변경되면 자동 업데이트
 - method : 호출해야만 실행됨

## Conditional Rendering

 - v-if : 표현식 값의 T/F를 기반으로 요소를 조건부로 렌더링
 ```HTML
  <p v-if="isSeen">true일때 보여요</p>
  <p v-else="isSeen">false일때 보여요</p>
  <button @click="isSeen = !isSeen">토글</button>
  <script>
    const isSeen = ref(true)
  </script>
 ```

 - v-if는 directive이기 때문에 단일 요소에만 연결 가능
 - 이 경우 template 요소에 -if를 사용하여 하나 이상의 요소에 대해 적용할 수 있음( v-else, v-else-if 모두 적용 가능)
 - HTML <template> element
   - 페이지가 로드 될 때 렌더링 되지 않지만 JavaScript를 사용하여 나중에 문서에서 사용할 수 있도록하는 HTML을 보유하기 위한 메커니즘
   - 보이지 않는 wrapper 역할

 - v-show : 표현식 값의 T/F를 기반으로 요소의 가시성을 전환

### v-if vs v-show

 - v-if(Cheap inital load, expensive toggle)
   - 초기 조건이 false인 경우 아무 작업도 수행하지 않음
   - 토글 비용이 높음

 - v-show(Expensive inital load, cheap toggle)
   - 초기 조건에 관계 없이 항상 렌더링
   - 초기 렌더링 비용이 더 높음

## List Rendering

 - v-for : 소스 데이터를 기반으로 요소 또는 템플릿 블록을 여러 번 렌더링
 - v-for는 alias in expression 형식의 특수 구문을 사용하여 반복되는 현재 요소에 대한 별칭(alias)을 제공
   ```HTML
      <div v-for="item in items">
        {{ item.text }}
      </div>
      <div v-for="(item, index) in items"></div>
      <div v-for="(value, key) in items"></div>
      <div v-for="(value, key, index) in items"></div>
   ```
 - 중첩된 v-for
   - 각 v-for 범위는 상위 범위에 접근 할 수 있음
   ```HTML
      <ul v-for="item in myInfo">
        <li v-for="friend in item.friend">
          {{ friend }}
        </li>
      </ul>
   ```

 - v-for와 key는 함께 사용한다 => 내부 컴포넌트 상태를 일관되게 유지
 - key는 반드시 각 요소에 대한 고유값을 나타낼 수 있는 식별자여야 함
 ```HTML
    <div v-for="item in items" :key="item.id">
      {{ item }}
    </div>
    <script>
      let id = 0
      const items = ref({
        { id: id++, name: "Alice"},
        { id: id++, name: "Bella"},
      })
    </script>
 ```

## v-for 와 v-if

 - 동일한 요소에 v-for와 v-if를 함께 사용하지 않는다.
   - 동일한 요소에 v-if가 v-for보다 우선순위가 더 높기 때문

 - v-for 와 v-if 문제 상황
   ```HTML
      <ul>
        <li v-for="todo in todos" v-if="!todos.isComplete" :key="todo.id">
          {{ todo.name }}
        </li>
      </ul>
      <!-- v-for with v-if & computed -->
      <ul>
        <li v-for="todo in completeTodos" :key="todo.id">
          {{ todo.name }}
        </li>
      </ul>
      <!-- v-for with v-if & template -->
      <ul>
        <template v-if="!todo.isComplete">
          <li v-for="todo in todos" :key="todo.id">
            {{ todo.name }}
          </li>
        </template>
      </ul>
      <script>
        let id = 0
        const todos = ref([
          { id: id++, name: "복습", isComplete: true},
          { id: id++, name: "예습", isComplete: false},
          { id: id++, name: "저녁식사", isComplete: true},
          { id: id++, name: "노래방", isComplete: false},
        ])

        const completeTodos = computed(() => {
          return todos.value.filter((todo) => !todo.isComplete)
        })
      </script>
   ```

## Watchers

 - watch() : 반응형 데이터를 감시하고, 감시하는 데이터가 변경되면 콜백 함수를 호출
 - watch 구조
   ```JS
    const { createApp, ref, watch } = Vue
    const count = ref(0)
    const countWatch = watch(count,(newValue, oldValue) => {
      console.log(`newValue : ${newValue}, oldValue: ${oldValue}`)
    })
    watch(variable, (newValue, oldValue) => {
      // do something
    })

    // message

    const message = ref("")
    const messageLength = ref(0)

    const messageWatch = watch(message, (newValue, oldValue) => {
      messageLength.value = newValue.length
    })
   ```

  - variable : 감시하는 변수
  - newValue : 감시하는 변수가 변화된 값, 콜백 함수의 첫번째 인자
  - oldValue : 콜백 함수의 두번째 인자

### Computed와 Watchers

 X | Computed | Watchers
---------|----------|---------
 공통점 | 데이터 변화를 감지하고 처리 | 동일
 동작 | 의존하는 데이터 속성의 계산된 값을 반환 | 특정 데이터 속성의 변화를 감시하고 작업을 수행
 사용 목적 | 템플릿 내에서 사용되는 데이터 연산용 | 데이터 변경에 따른 특정 작업 처리용
 사용 예시 | 연산 된 길이, 필터링 된 목록 계산 등 | 비동기 API 요청, 연관 데이터 업데이트

## Lifecycle Hooks

 - createApp ~ 메모리에서 삭제 ( 프로그램 종료 )
 - 

 - Vue 인스턴스의 생애주기 동안 특정 시점에 실행되는 함수
 ```JS
    const { createApp, ref, onMounted, onUpdated } = Vue

    const app = createApp({
      setup() {
        const count = ref(0)
        const message = ref(null)

        onMounted(() => {
          console.log("mounted")
        })

        onUpdated(() => {
          message.value = "updated!"
        })

        return {
          count,
          message
        }
      },
    })
 ```