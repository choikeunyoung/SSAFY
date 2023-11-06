## Templae Syntax

 2. Raw HTML
    ```HTML
        <div v-html="rawHtml"></div>
        <script>
            ref("<span style='color:red'>This should be red</span>")
        </script>
    ```
 3. Attribute Bindings
    ```HTML
        <div v-bind: id="dynamicId"></div>
        <script>
            const dynamicId = ref("my-id")
        </script>
    ```
 4. JavaScript Expressions
    ```HTML
        <div>{{ number + 1 }}</div>
        <div>{{ ok ? "YES" : "NO" }}</div>
        <div>{{ meg.split("").reverse().join('') }}</div>
        <div v-bind: id="`list-${id}`"></div>
        <script>
            const msg = ref("Hello")
            const number = ref(1)
            const ok = ref(true)
            const id = ref(100)
        </script>
    ```

### Expressions 주의사항

 - 각 바인딩에는 하나의 단일 표현식만 포함될 수 있음
   - 표현식은 값으로 평가할 수 있는 코드 조각 (return 뒤에 사용할 수 있는 코드여야 함)
 - 작동하지 않는 경우
 ```HTML
    <!-- 표현식이 아닌 선언식 -->
    {{ const number = 1}}
    <!-- 흐름제어도 작동하지 않음. 삼항 표현식을 사용 -->
    {{ if (ok) { return message } }}
 ```

## Directive

 - 'v-'접두사가 있는 특수 속성
 - Directive의 속성 값은 단일 JavaScript 표현식이어야 함 (v-for, v-on 제외)
 - 표현식 값이 변경될 때 DOM에 반응적으로 업데이트를 적용
 - v-if 는 seen 표현식 값의 T/F를 기반으로 <p> 요소를 제거/삽입
   ```HTML
    <p v-if="seen">Hi There</p>
   ```

### Directive 전체 구문

 - v-on : submit.prevent = "onSubmit"
 - v-on => Name
 - submit => Argument
 - prevent => Modifiers
 - onSubmit => Value

### Directive - Arguments

 - 일부 directive는 directive 뒤에 콜론(:)으로 표시되는 인자를 사용할 수 있음
 - 아래 예시의 href는 HTML a 요소의 href 속성 값을 myUrl 값에 바인딩 하도록 하는 v-bind의 인자
 ```HTML
    <a v-bind:href="myUrl">Link</a>
    <button v-on:click="doSomething">Button</button>
 ```

### Directive - Modifiers

 - .(dot)로 표시되는 특수 접미사로, directive가 특별한 방식으로 바인딩되어야 함을 나타냄
 - 예를 들어 .prevent는 발생한 이벤트에서 event.preventDefault()를 호출하도록 v-on에 지시하는 modifier
 ```HTML
    <form @submit.prevent="onSubmit">...</form>
 ```

## Dynamically data binding

 - v-bind : 하나 이상의 속성 또는 컴포넌트 데이터를 표현식에 동적으로 바인딩

 1. Attribute Bindings
    - <img v-bind:src="imageSrc">
    - <a v-bind:href="myUrl">Move to url</a>
    - Dynamic attribute name (동적 인자 이름)
    - 대괄호로 감싸서 directive argument에 JavaScript 표현식을 사용할 수 있음
    - JavaScript 표현식에 따라 동적으로 평가된 값이 최종 argument 값으로 사용됨
    - <button :[key]="myValue">Button</button>
    - 대괄호 안에 작성하는 이름은 반드시 소문자!!

 2. Class and Style Bindings
    - 객체를 class에 전달하여 클래스를 동적으로 전환할 수 있음
    ```HTML
        <div :class="{ active: isActive }">Text</div>
    ```

    - 객체를 더 많은 필드를 포함하여 여러 클래스를 전환할 수 있음
    ```HTML
        <div :class="{ active: isActive, `text-primary`: hasInfo }">Text</div>
        <div :class="classObj">Text</div>
        <script>
            const classObj = ref({
                active : isActive,
                `text-primary` : hasInfo
            })
        </script>
    ```

    - 배열에 바인딩하여 클래스 목록을 적용할 수 있음
    ```HTML
        <div :class="[activeClass, infoClass]">Text</div>
        <div :class="[{ active : isActive }]">Text</div>
    ```

    - style은 JavaScript 객체 값에 대한 바인딩을 지원
    - 실제 CSS에서 사용하는 것처럼 :style은 kebab-cased 키 문자열도 지원 camelCase 작성 권장
    ```HTML
        <div :style="{ color : activeColor, fontSize: fontSize = 'px'}">Text</div>
        <div :style="{ `font-size` : fontSize + 'px' }">Text</div>
        <div :style="styleObj">
        <script>
            const activeColor = ref("crimson");
            const fontSize = ref(50)
            const styleObj = ref({
                color: activeColor,
                fontSize : fontSize.value + 'px'
            })
            return {
                activeColor,
                fontSize,
                styleObj
            }
        </script>
    ```

    - 여러 스타일 객체의 배열에 :style을 바인딩 할 수 있음
    ```HTML
        <div :style="[styleObj, styleObj2]">Text</div>
        <script>
        const styleObj2 = ref({
            color: 'blue',
            border: '1px solid black'
        })
        return styleObj2
        </script>
    ```

## Event Handling

 - v-on
 - handler 종류
   1. Inline handlers : 간단한 상황에서 사용
      - 메서드 이름에 직접 바인딩하는대신 Inline Handlers에서 메서드를 호출할 수 있음
   2. Method Handlers : Inline handlers로 불가능한 대부분의 상황