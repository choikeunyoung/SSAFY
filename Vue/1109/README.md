# Router

 1. Routing
 2. Vue Router
 3. Navigation Guard

## Routing

 - 네트워크에서 경로를 선택하는 프로세스
 - SSR에서의 Routing
   - 서버가 사용자가 방문한 URL 경로를 기반으로 응답을 전송
   - 링크를 클릭하면 브라우저는 서버로부터 HTML 응답을 수신하고 새 HTML로 전체 페이지를 다시 로드
 - CSR/SPA에서 Routing
   - SPA에서 Routing은 브라우저의 클라이언트 측에서 수행
   - 클라이언트 측 JavaScript가 새 데이터를 동적으로 가져와 전체 페이즈를 다시 로드 하지 않음
   - 페이지는 1개이지만, 링크에 따라 여러 컴포넌트를 렌더링하여 마치 여러 페이지를 사용하는 것처럼 보이도록 해야 함

 - routing이 없다면
   - 유저가 URL을 통한 페이지의 변화를 감지할 수 없음
   - 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음
     - URL이 1개이기 떄문에 새로 고침 시 처음 페이지로 되돌아감
     - 링크를 공유할 시 첫 페이지만 공유 가능
   - 브라우저의 뒤로 가기 기능을 사용할 수 없음

## Vue Router

 - Vue 공식 라우터
 - RouterLink
   - 페이지를 다시 로드 하지 않고 URL을 변경하고 생성 및 관리 로직을 철
   - HTML의 a 태그를 렌더링
   ```Vue
    <template>
        <header>
            <nav>
                <RouterLink to="/">Home</RouterLink>
                <RouterLink to="/about">About</RouterLink>
            </nav>
        </header>
        <RouterView />
    </template>
   ```

 - RouterView
   - URL에 해당하는 컴포넌트를 표시
   - 어디에나 배치하여 레이아웃에 맞출 수 있음
 - router/index.js
   - 라우팅에 관련된 정보 및 설정이 작성 되는 곳
   - router에 URL과 컴포넌트를 매핑
 - views
   - RouterView 위치에 렌더링 할 컴포넌트를 배치
   - 기존 components 폴더와 기능적으로 다른 것은 없으며 단순 분류의 의미로 구성됨

### Basic Routing

 - index.js에 라우터 관련 설정 작성(주소, 이름, 컴포넌트)
 - RouterLink의 'to' 속성으로 index.js에서 정의한 주소 속성 값(path)을 사용
 ```vue
    <template>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/about">About</RouterLink>
    </template>
    <script setup>
        // index.js
        const router = createRouter({
            routes: [
                {
                    path: "/",
                    name: "home",
                    component : HomeView
                },
            ]
        })
    </script>
    
 ```

### Named Routes

 - 경로에 이름을 지정하는 라우팅
 - name 속성 값에 경로에 대한 이름을 지정
 - 경로에 연결하려면 RouterLink에 v-bind를 사용해 "to" prop 객체로 전달
 - 하드 코딩 된 URL을 사용하지 않아도 됨
 ```vue
    <template>
    <RouterLink :to="{ name : 'home' }">Home</RouterLink>
    <RouterLink :to="{ name : "about" }">About</RouterLink>
    </template>
    <script setup>
        // index.js
        const router = createRouter({
            routes: [
                {
                    path: "/",
                    name: "home",
                    component : HomeView
                },
            ]
        })
    </script>
 ```

### Dynamic Route Matching with Params

 - 매개 변수를 사용한 동적 경로 매칭
 - 주어진 패턴 경로를 동일한 컴포넌트에 매핑 해야 하는 경우 활용
 - 매개변수는 콜론(:)으로 표기
 ```JS
    // index.js
    import UserView from "../views/UserView.vue"

    const router = createRouter({
        routes: [
            {
                path: 'user/:id',
                nama: 'user',
                component: userView
            },
        ]
    })
 ```

 - 동적 경로 매칭 활용
 ```HTML
    <template>
        <div>
            <h1>UserView</h1>
            <h2>{{ userId }}번 User 페이지</h2>
        </div>
    </template>
 ```
 ```JS
    import { ref } from 'vue'
    import { useRoute } from 'vue-router'

    const route = useRoute()
    const userId = ref(route.params.id)
 ```

### Programmatic Navigations

 - router의 인스턴스 메서드를 사용해 RouterLink로 a 태그를 만드는 것처럼 프로그래밍으로 네비게이션 관련 작업을 수행할 수 있음
 
 1. 다른 위치로 이동하기 => router.push()
    - 다른 URL로 이동하는 메서드
    - 새 항목을 history stack에 push하므로 사용자가 브라우저 뒤로 가기 버튼을 클릭하면 이전 URL로 이동할 수 있음
    - RouterLink를 클릭했을 떄 내부적으로 호출되는 메서드 이므로 RouterLink를 클릭하는 것은 router.push()를 호출하는 것과 같음

    선언적 | 프로그래밍적 
    ---------|----------
     `<RouterLink :to="...">` | router.push(...) 

    ```JS
    // literal string path
    router.push("/user/alice")
    // object with path
    router.push({ path: "/users/alice"})
    // named route with params to let the router build the url
    router.push({ name: 'user', params: { username: 'alice'}})
    // with query, resulting in /register?plan=private
    router.push({ path: '/register', query: { plan: 'private'}})
    ```

 2. 현재 위치 바꾸기 => router.replace()
    - push 메서드와 달리 histroy stack에 새로운 항목을 push 하지 않고 다른 URL로 이동 (=== 이동 전 URL로 뒤로 가기 불가)

    선언적 | 프로그래밍적 
    ---------|----------
     `<RouterLink :to="..." replace>` | router.replace(...)

## Navigation Guard

 - Vue router를 통해 특정 URL에 접근할 때 다른 URL로 redirect를 하거나 취소하여 네비게이션을 보호

 1. Globally(전역 가드)
    - 애플리케이션 전역에서 동작
    - index.js에서 정의

 2. Per-route(라우터 가드)
    - 특정 route에서만 동작
    - index.js의 각 routes에 정의

 3. In-component(컴포넌트 가드)
    - 특정 컴포넌트 내에서만 동작
    - 컴포넌트 Script에 정의

### Globally Guard

 - router.beforeEach() => 다른 URL로 이동하기 직전에 실행되는 함수
 - 구조
   ```JS
    router.beforeEach((to, from) => {
        ...
        return false
    })
   ```
   - to : 이동 할 URL 정보가 담긴 Route 객체
   - from : 현재 URL 정보가 담긴 Route 객체
   - 선택적 반환(return) 값
     1. false
        - 현재 네비게이션을 취소
        - 브라우저 URL이 변경된 경우(사용자가 수동으로 또는 뒤로 버튼을 통해) from 경로의 URL로 재설정
     2. Route Location
        - router.push()를 호출하는 것처럼 경로 위치를 전달하여 다른 위치로 redirect
        ```JS
        router.beforeEach((to, from) => {
            ...
            return { name : "About" }
        })
        ```

### Per-route Guard

 - router.beforeEnter() => route에 진입했을 때만 실행되는 함수
 ```JS
    {
        path: '/user/:id',
        name: 'user',
        component: UserView,
        beforeEnter: (to, from) => {
            ...,
            return false
        }
    }
 ```
 - 함수의 to, from, 선택 반환 인자는 beforeEach와 동일

### In-component Guard

 - onBeforeRouteLeave
   - 현재 라우트에서 다른 라우트로 이동하기 전에 실행
   ```JS
    import { onBeforeRouteLeave } from "vue-router"

    onBeforeRouteLeave((to, from) => {
        const answer = window.confirm("정말 떠나실 건가요?")
        if (answer == false) {
            return false
        }
    })
   ```

 - onBeforeRouteUpdate
   - 이미 렌더링된 컴포넌트가 같은 라우트 내에서 업데이트되기 전에 실행
   ```JS
    import { onBeforeRouteLeave, onBeforeRouteUpdata } from 'vue-router'

    const routeUpdate = function() {
        router.push({ name: 'user', params: { id: 100}})
    }

    onBeforeRouteUpdate((to, from) => {
        userId.value = to.params.id
    })
   ```

## 참고

 - Lazy Loading Routes
   - 첫 빌드 시 해당 컴포넌트를 로드 하지 않고, 해당 경로를 처음 방문할 떄 컴포넌트를 로드 하는 것
   - 기존의 정적 방식 => 동적 방식으로 변경하는 것과 같음
   ```JS
    path: '/about',
    name: 'about',
    component: () => import("../views/AboutView.vue")
   ```