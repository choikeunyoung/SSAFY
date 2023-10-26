# event


## addEventListener

 EventTarget.addEventListener(type, handler)

 - type : 수신할 이벤트, 문자열로 작성(ex. "click")
 - handler : 이벤트 객체를 수신하는 콜백 함수, 발생한 Event object를 유일한 매개변수로 받음
 - 대상에 특정 Event가 발생하면, 지정한 이벤트를 받아 할 일을 등록한다.
 - 발생한 이벤트를 나타내는 Event 객체를 유일한 매개변수로 받고 아무것도 반환하지 않는다.

## 버블링

 - 한 요소에 이벤트가 발생하면, 이 요소에 할당된 핸들러가 동작하고, 이어 부모 요소의 핸들러가 동작하는 현상
 - 가장 최상단의 조상 요소(document)를 만날 때까지 이 과정이 반복되면서 요소 각각에 할당된 핸들러가 동작

## target & currentTarget 속성

 - target 속성
   - 이벤트가 발생한 가장 안쪽의 요소(target)를 참조하는 속성
   - 실제 이벤트가 시작된 target 요소
   - 버블링이 진행 되어도 변하지 않음

 - currentTarget 속성
   - 현재 요소
   - 항상 이벤트 핸들러가 연결된 요소만을 참조하는 속성
   - this와 같음

## event handler 활용

 1. 버튼을 클릭하면 숫자를 1씩 증가해서 출력하기
 2. 사용자의 입력 값을 실시간으로 출력하기
 3. 사용자의 입력 값을 실시간으로 출력 "+" 버튼 클릭하면 출력한 값의 CSS 스타일을 변경하기
 4. todo 프로그램의 구현
 5. 로또 번호 생성기 구현