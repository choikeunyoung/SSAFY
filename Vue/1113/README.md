## State Management

 - Vue 컴포넌트는 이미 반응형 상태를 관리하고 있음 (상태 === 데이터)
 - 상태(State)
   - 앱 구동에 필요한 기본 데이터
 - 뷰(View)
   - 상태를 선언적으로 매핑하여 시각화
 - 기능(Actions)
   - 뷰에서 사용자 입력에 대해 반응적으로 상태를 변경할 수 있게 정의된 동작
 - 상태 관리의 단순성이 무너지는 시점
   - 여러 컴포넌트가 상태를 공유할 때
   - 여러 뷰가 동일한 상태에 종속되는 경우
   - 서로 다른 뷰의 기능이 동일한 상태를 변경시켜야 하는 경우

## State management library(Pinia)

 - Vue 공식 상태 라이브러리
 - Vite 프로젝트 빌드 시 Pinia 라이브러리 추가
 - Pinia는 store라는 저장소를 가짐
 - store는 state, getters, actions으로 이루어지며 각각 ref(), computed(), function() 과 동일

### State

 - store 인스턴스로 state에 접근하여 직접 읽고 쓸 수 있음
 - store에 state를 정의하지 않았다면 컴포넌트에 새로 추가할 수 없음

### Getters

 - store의 모든 getters를 state 처럼 직접 접근 할 수 있음

### Actions

 - store의 모든 actions를 직접 접근 및 호출 할 수 있음
 - getters와 달리 state 조작, 비동기, API 호출이나 다른 로직을 진행할 수 있음