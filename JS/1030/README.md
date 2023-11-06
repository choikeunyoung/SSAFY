# OS 지식

 - 동기 VS 비동기 / 동시에 일을 처리하는 것은 다른 개념
 - Synchronous, Asynchrounous, Blocking, Non-Blocking
   - 비슷한 개념이라 혼동 주의

## 동기적(Synchronous) vs 비동기적(Asynchrounous)

 - 순서대로 일이 마치는가 ? 에 대한 여부
 - A -> B -> C 함수가 순서대로 호출 되었을 때, 순서대로 끝나는가?
 - 실행 순서와 끝나는 순서가 동일한가에 대한 구분

## Blocking vs Non-Blocking

 - 동시에 작업을 할 수 있는가?
 - A -> B 함수를 호출
   - A 가 실행되는 도중에 B 함수가 아무것도 못하면 Blocking
   - A 가 실행되는 도중에 B 함수도 자기 일을 동시에 진행한다면 Non-Blocking

 1. 일을 시키고 바로 밥을 먹으러 감
    - 일의 진행과 동시에 밥을 먹는 것 ( Non-Blocking )
    1.1 밥을 먹는 중, 일이 끝났다고 전화를 함
      - 끝나는 순서가 동일 ( Syschronous )
      - Non-Blocking - Syschronous

    1.2 밥을 먹고 와서 일에 대한 결과를 들음
      - 끝나는 순서가 바뀜 ( Asynchrounous )
      - NonBlocking - Asynchrounous

 2. 일이 끝날 때 까지 기다렸다가, 결과를 듣고 밥을 먹으러 감
    - 밥을 동시에 먹지 못함 ( Blocking )
    - 동시에 처리를 못함 -> 끝나는 순서가 무조건 보장
      - Blocking -> Synchronous

 - Blocking - Asynchrounous
   - 실제 사례를 생각해 봐도 잘 안떠오름
   - NonBlocking-Asynchrounous 방식 사용중 하나라도 Blocking 요소가 존재한다면, 의도치 않게 Blocking-Asynchrounous 가 발생가능

## 프로세스와 쓰레드

 - 자바스크립트는 Single Thread 기반 언어이다.
 - 완벽히 이해하기 보다는 이런 것이 있다.
   - 나중에 OS 공부를 본격적으로 할 때 다시 학습하는 것을 추천

## 프로세스(Process)
 - 실행 중에 있는 프로그램
   - 프로그램 : 보조 기억장치에 저장되어 있음
     - 실행되기를 기다리는 명령어와 정적인 데이터의 묶음
   - 더블클릭 등으로 프로그램을 실행하면
     - 실행을 위해서 주기억장치(RAM)에 메모리 할당
     - 이때부터 프로세스라고 부름

## 쓰레드(Thread)
 - 프로세스 내부에서 실제로 작업을 하는 주체
 - 작업의 단위, 흐름이라고도 표현함
 - 프로그램을 작동시키기 위해 필요한 자원들이 존재(메모리, CPU 할당 등)
   - 이러한 자원을 실제로 이용하는 단위
 - 즉, 하나의 프로세스는 하나 이상의 쓰레드로 구성

## 멀티 프로세스
 - 여러 프로그램을 동시에 실행하는 기법
 - CPU는 한 번에 하나의 연산만 수행 가능
   - 연산이 너무 빨라서 동시에 작업하는 것으로 보이는 것

## 멀티 쓰레드
 - 하나의 프로세스 내에서 동시에 여러 쓰레드로 작업을 실행
   - 유튜브 라이브 : 영상 시청 + 채팅 입력 + 채팅 확인
 - 쓰레드끼리는 프로세스 내의 자원을 공유함
   - 동시성 문제
     - 공유된 자원에 동시에 여러 쓰레드가 접근하는 경우
 - 동시화 기법 : 뮤텍스(Mutex), 세마포어(Semaphore)

# Asynchronous JavaScript

 1. 비동기
 2. JavaScript와 비동기
 3. AJAX
 4. Callback과 Promise

## 비동기

 - Synchronous(동기) : 프로그램의 실행 흐름이 순차적으로 진행
 - Asynchronous(비동기) : 프로그램의 실행 흐름이 순차적이지 않으며, 작업이 완료되기를 기다리지 않고 다음 작업이 실행되는 방식
 - 병렬적 수행
 - 당장 처리를 완료할 수 없고 시간이 필요한 작업들은 별도로 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리

## JavaScript와 비동기

 - Single Thread 언어, JavaScript
 - Thread란? : 작업을 처리할 때 실제로 작업을 수행하는 주체로, multi-thread라면 업무를 수행할 수 있는 주체가 여러 개라는 의미
 - JavaScript는 한 번에 하나의 일만 수행할 수 있는 Single Thread 언어로 동시에 여러 작업을 처리할 수 없음
 - 요청 순서대로 처리할 수 밖에 없다.
 - JavaScript Runtime
   - 동작할 수 있는 환경(Runtime)
   - JavaScript 자체는 Single Thread이므로 비동기 처리를 할 수 있도록 도와주는 환경이 필요
   - JavaScript에서 비동기와 관련한 작업은 "브라우저" 또는 "Node"와 같은 환경에서 처리
 - 브라우저 환경에서 JavaScript 비동기 처리 관련 요소
   1. JavaScript Engine의 Call Stack
   2. Web API
   3. Task Queue
   4. Event Loop

 - 브라우저 환경에서 JavaScript 비동기 처리 동작 방식
    1. 모든 작업은 Call Stack(LIFO)으로 들어간 후 처리된다.
    2. 오래 걸리는 작업이 Call Stack으로 들어오면 Web API로 보내 별도로 처리하도록 한다.
    3. Web API에서 처리가 끝난 작업들은 곧바로 Call Stack으로 들어가지 못하고 Task Queue(FIFO)에 순서대로 들어간다.
    4. Event Loop가 Call Stack이 비어 있는 것을 계속 체크하고 Call Stack이 빈다면 Task Queue에서 가장 오래된(가장 먼저 처리되어 들어온) 작업을 Call Stack으로 보낸다.

 - 비동기 처리 동작 요소
   1. Call Stack
      - 요청이 들어올 때 마다 순차적으로 처리하는 Stack(LIFO)
      - 기본적인 JavaScript의 Single Thread 작업 처리

   2. Web API
      - JavaScript 엔진이 아닌 브라우저에서 제공하는 runtime 환경
      - 시간이 소요되는 작업을 처리 (setTimeout, DOM Event, AJAX 요청 등)

   3. Task Queue(Callback Queue)
      - 비동기 처리된 Callback 함수가 대기하는 Queue(FIFO)

   4. Event Loop
      - 태스크(작업)가 들어오길 기다렸다가 태스크가 들어오면 이를 처리하고, 처리할 태스크가 없으면 잠드는, 끊임없이 돌아가는 자바스크립트 루프
      - Call Stack과 Task Queue를 지속적으로 모니터링
      - Call Stack이 비어 있는지 확인 후 비어 있다면 Task Queue에서 대기 중인 오래된 작업을 Call Stack으로 Push

## AJAX(Asynchronous JavaScript + XML)

 - JavaScript의 비동기 구조와 XML 객체를 활용해 비동기적으로 서버와 통신하여 웹 페이지의 일부분만을 업데이트하는 웹 개발 기술
 - XMLHttpRequest 객체 : 서버와 상호작용할 때 사용하며 페이지의 새로고침 없이도 URL에서 데이터를 가져올 수 있음
 - 이벤트 핸들러는 비동기 프로그래밍의 한 형태
   - 이벤트가 발생할 때마다 호출되는 함수(콜백 함수)를 제공하는 것
   - XMLHttpRequest(XHR)는 JavaScript를 사용하여 서버에 HTTP 요청을 할 수 있는 객체
   - HTTP 요청은 응답이 올때까지의 시간이 걸릴 수 있는 작업이라 비동기 API이며, 이벤트 핸들러를 XHR 객체에 연결해 요청의 진행 상태 및 최종 완료에 대한 응답을 받음

## Axios

 - JavaScript에서 사용되는 Promise 기반의 HTTP 클라이언트 라이브러리
 - get, post 등 여러 http request method 사용가능
 - then 메서드를 사용해서 " 성공하면 수행할 로직 " 을 작성
 - catch 메서드를 사용해서 " 실패하면 수행할 로직 " 을 작성

## Callback과 Promise

 - 비동기 처리의 단점
   - 비동기 처리의 핵심은 Web API로 들어오는 순서가 아니라 작업이 완료되는 순서에 따라 처리한다는 것
   - 이는 개발자 입장에서 코드의 실행 순서가 불명확하다는 단점 존재
   - 이와 같은 단점은 실행 결과를 예상하면서 코드를 작성할 수 없게 함
 - 비동기 콜백
   - 비동기적으로 처리되는 작업이 완료되었을 때 실행되는 함수
   - 연쇄적으로 발생하는 비동기 작업을 순차적으로 동작할 수 있게 함
 - 비동기 콜백의 한계
   - 콜백 지옥(Callback Hell)
     - 비동기 처리를 위한 콜백을 작성할 때 마주하는 문제
     - 코드 작성 형태가 마치 피라미드와 같다고 해서 Pyramid of doom(파멸의 피라미드) 라고 부름
   - 비동기 콜백 함수는 보통 어떤 기능의 실행 결과를 받아서 다른 기능을 수행하기 위해 많이 사용

## Promise

 - JavaScript에서 비동기 작업의 결과를 나타내는 객체
 - 콜백 지옥 문제를 해결하기 위해 등장한 비동기 처리를 위한 객체
 - 작업이 끝나면 실행 시켜 줄게 라는 약속
 - 비동기 작업의 완료 또는 실패를 나타내는 객체
 - Promise 기반의 클라이언트가 바로 이전에 사용한 Axios 라이브러리
   - 성공하면 then()
   - 실패하면 catch()
 - then(callback)
   - 요청 작업이 성공하면 callback 실행
   - callback은 이전 작업의 성공 결과를 인자로 전달 받음
 - catch(callback)
   - then()이 하나라도 실패하면 callback 실행
   - callback은 이전 작업의 실패 객체를 인자로 전달 받음
 - then과 catch는 모두 항상 promise 객체를 반환
 - 계속해서 chaining을 할 수 있음
 - axios로 처리한 비동기 로직이 항상 promise 객체를 반환
 - then을 계속 이어 나가면서 작성할 수 있게 됨
 - then 메서드 chaining의 목적
   - 비동기 작업의 순차적 처리 가능
   - 코드를 보다 직관적이고 가독성 좋게 작성할 수 있도록 도움

 - then 메서드 chaining의 장점
   1. 가독성
      - 비동기 작업의 순서와 의존 관계를 명확히 표현할 수 있어 코드의 가독성 향상
   2. 에러 처리
      - 각각 비동기 작업 단계에서 발생하는 에러를 분할에서 처리 가능
   3. 유연성
      - 각 단계마다 필요한 데이터를 가공하거나 다른 비동기 작업을 수행할 수 있어서 더 복잡한 비동기 흐름을 구성할 수 있음
   4. 코드 관리
      - 비동기 작업을 분리하여 구성하면 코드를 관리하기 용이

    ```JS
      .then((response) => {
        imgUrl = response.data[0].url
        return imgUrl
      })
      .then((imgData) => {
        imgElem = document.createElement("img")
        imgElem.setAttribute('src', imgData)
        document.body.appendChild(imgElem)
      })
      // 첫번째 then 콜백함수의 반환 값이 이어지는 then 콜백함수의 인자로 전달됨
    ```
  
### Promise가 보장하는 것 (vs 비동기 콜백)

 1. 콜백 함수는 JavaScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출되지 않음
    - 반면 Promise callback 함수는 Event Queue에 배치되는 엄격한 순서로 호출됨

 2. 비동기 작업이 성공하거나 실패한 뒤 .then() 메서드를 이용하여 추가한 경우에도 호출 순서를 보장하며 동작

 3. .then()을 여러 번 사용하여 여러 개의 callback 함수를 추가할 수 있음
    - 각각의 callback은 주어진 순서대로 하나하나 실행하게 됨
    - Chaining은 Promise의 가장 뛰어난 장점