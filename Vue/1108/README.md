# Component State Flow

 1. Passing Props
 2. Component Events

## Passing Props

 - One-Way Data Flow : 모든 props는 자식 속성과 부모 속성 사이에 하향식 단방향 바인딩을 형성
 - 부모 속성이 업데이트되면 자식으로 흐르지만 그 반대는 안됨
 - 자식 컴포넌트 내부에서 props를 변경하려고 시도해서는 안되며 불가능
 - 부모 컴포넌트가 업데이트될 때마다 자식 컴포넌트의 모든 props가 최신 값으로 업데이트 됨
 - 단방향인 이유
   - 하위 컴포넌트가 실수로 상위 컴포넌트의 상태를 변경하여 앱에서 데이터 흐름을 이해하기 어렵게 만드는 것을 방지하기 위함

### Props 선언

 - 부모 컴포넌트에서 보낸 props를 사용하기 위해서는 자식 컴포넌트에서 명시적인 props 선언이 필요
 ```vue
   <!-- Parent.vue -->
   <template>
    <div>
      <ParentChild my-msg="message" />
    </div>
   </template>
   <!-- prop 이름 : my-msg / prop 값 : message -->
 ```

### Props 선언 2가지 방식

 1. 문자열 배열을 사용한 선언
  - defineProps()를 사용하여 props를 선언
  ```vue
    <script setup>
      defineProps(['myMsg'])
    </script>
  ```
 2. 객체를 사용한 선언
 - 객체 선언 문법의 각 객체 속성의 키는 props의 이름이 되며, 객체 속성의 값은 값이 될 데이터의 타입에 해당하는 생성자 함수(Number, String)여야 함
 ```vue
    <script setup>
      defineProps({
        myMsg : String
      })
    </script>
 ```

### prop 데이터 사용

 - 템플릿에서 반응형 변수와 같은 방식으로 활용
 ```vue
 <!-- ParentChild.vue -->
  <div>
    <p>{{ myMsg }}</p>
  </div>
  <script>
    const props = defineProps({ myMsg : String })
    console.log(props) // {myMsg : "message"}
    console.log(props.myMsg) // "message"
  </script>
 ```

### Props 세부사항

 1. Props Name Casing (Props 이름 컨벤션)
    - 선언 및 템플릿 참조 시 (camelCase)
    ```Vue
      <p>{{ myMsg }}</p>
      <script>
        defineProps({
          myMsg : String,
        })
      </script>
    ```
    - 자식 컴포넌트 전달 시 (kebab-case)
    ```vue
      <ParentChild my-msg="message" />
    ```

 2. Static Props & Dynamic Props
    - 지금까지 작성한 것은 Static(정적) props
    - v-bind를 사용하여 동적으로 할당된 props를 사용할 수 있음

    1. Dynamic Props 정의
    ```Vue
      <ParentChild my-msg="message" :dynamit-props="name" />
      <script>
      import { ref } from "vue"
      const name = ref("Alice");
      </script>
    ```

    2. Dynamic props 선언 및 출력
    ```vue
      <!-- ParentChild.vue -->
      <p>{{ dynamicProps }}</p>
      <script>
        defineProps({
          myMsg : String,
          dynamicProps : String,
        })
      </script>
    ```

## Component Events

 - $emit() : 자식 컴포넌트가 이벤트를 발생시켜 부모 컴포넌트로 데이터를 전달하는 역할의 메서드
   - 메서드 구조 => $emit(event, ...args)
     - event : 커스텀 이벤트 이름
     - args : 추가 인자

### Event 발신 및 수신

 - $emit을 사용하여 템플릿 표현식에서 직접 사용자 정의 이벤트를 발신
 ```vue
  <button @click="$emit("someEvent")">클릭</button>
 ```
 - 부모는 v-on을 사용하여 수신할 수 있음
 ```vue
  <ParentComp @some-event="someCallback" />
 ```

## emit Event 선언

 - defineEmits()를 사용하여 명시적으로 발신할 이벤트를 선언할 수 있음
 - script에서 $emit 메서드를 접근할 수 없기 때문에 defineEmits()는 $emit 대신 사용할 수 있는 동등한 함수를 반환

 ```vue
    <script setup>
      const emit = defineEmits(['someEvent', 'myFocus'])

      const buttonClick = function () {
        emit('someEvent')
      }
    </script>
 ```

 - 이벤트 선언하기
   ```vue
      <!-- ParentChild.vue -->
      <button @click="buttonClick">클릭</button>
      <script setup>
        const emit = defineEmits(['someEvent'])

        const buttonClick = function () {
          emit('someEvent')
        }
      </script>
   ```

## Event 인자

 - 이벤트 발신 시 추가 인자를 전달하여 값을 제공할 수 있음
 - ParentChild에서 이벤트를 발신하여 Parent로 추가 인자 전달하기
 ```vue
  <button @click="emitArgs">추가 인자 전달</button>
  <script>
    const emit = defineEmits(['someEvent', 'emitArgs'])
    const emitArgs = function () {
      emit("emitArgs", 1, 2, 3)
    }
  </script>
  <!-- Parent.vue -->
  <ParentChild @some-event="someCallback" @emit-args="getNumbers" my-msg = "message" :dynamic-props = "name" />
  <script>
    const getNumbers = function (...args) {
      console.log(args)
      console.log(`ParentChild가 전달한 추가인자 ${args}를 수신했어요.`)
    }
  </script>
 ```

### Event 세부사항

 - 선언 및 발신시 (camelCase)
 ```vue
  <ParentChild @some-event="..." />
  <button @click="$emit('someEvent')">클릭</button>
  <script>
    const emit = defineEmits(['someEvent'])
    emit('someEvent')
  </script>
 ```
 - 부모 컴포넌트에서 수신시 (kebab-case)