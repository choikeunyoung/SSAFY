# Single-File Components

 - 컴포넌트의 템플릿, 로직 및 스타일을 하나의 파일로 묶어낸 특수한 파일 형식

 1. Single-File Components
 2. SFC build tool (Vite)
 3. Vue Component
 4. 추가 주제

## NPM

 - pip 랑 동일한 역할 (자바스크립트 패키지 관리자)
 - lodash, axios -> cdn 으로 가져왔었음
 - 전역적으로 설치된 패키지를 관리
 - 현재 프로젝트만 패키지 관리 (nvm)

### npm 명령어

 - `npm init` : Node.js 패키지 관리, 초기화하는 도구
   - package.json 파일이 생성됨
 - `npm install` : 패키지를 설치하는 도구
   - package.json, package-lock.json 파일을 확인하여 필요한 패키지를 설치
 - `npm install <패키지명>` : 현재 프로젝트에 특정 패키지 추가
 - `npm install -g <패키지명>` : 전역 영역에 패키지 추가
 - `npm root` : 현재 프로젝트가 참조하고 있는 패키지 목록(node_modules) 확인
 - `npm audit` : 보안 및 의존성 취약점 해결하기위한 도구
   - 보안 취약점
     - 개발자가 악성 코드를 넣으면 그대로 노출됨
     - 최소한 보안 취약점을 검사해주기 위해 npm 에서 제공하는 명령어
   - 의존성 문제
     - 현재 프로젝트에 구성된 종속성에 대한 설명과 취약성에 대한 보고
     - [주의사항] aduit 명령어는 최소한의 해결법, 개발자가 추가로 확인해야함

### Vue 프로젝트 생성
 
 - TypeScript
   - 자바스크립트의 가장 큰 단점인 타입으로 인한 에러를 많이 없앤 버전
 - JSX
   - React 진영에서 만듬
   - HTML 요소를 변수로 담을 수 있음 -> 화면 구성이 매우 편리해짐
 - ESLint
   - 코드를 분석하여 문법적인 오류, 안티 패턴을 찾아주고 코드 스타일을 작성할 수 있도록 도와줌
   - 스타일 가이드를 적용해서 가이드를 따르지 않으면 잔소리 하도록 설정할 수 있음

### vite

 - 우리가 개발할 수 있도록 세팅하는데 도움을 주는 도구
 - [참고] vue-cli -> vue2 버전

### package.json의 의미

 - 프로젝트 종속성 목록과 빌드 도구 등 여러 구성 옵션이 작성되어 있음

 - `name` : 프로젝트 이름
 - `version` : 프로젝트의 버전
   - "1.2.3" : `[Major].[Minor].[Patch]`
     - Major : 기존 버전과 호환되지 않는 새로운 기능이 추가될 때 버전 업
     - Minor : 기존 버전과 호환되는 새로운 기능이 추가될 때 버전 업
     - Patch : 기존 버전과 호환되는버그 수정 및 기능 개선 시 버전 업
 - `private` : true 로 설정하면, npm 레지스트리에 해당 프로젝트를 배포할 수 없음
 - `scripts` : 프로젝트에서 실행할수 있는 실행 스크립트들을 정의하는 부분
   - vue 에서는 3가지 스크립트를 지원
   - `dev` : 개발 서버 실행
   - `build` : 배포 할 수 있는 형태로 만들어 줌
     - 코드 압축 등
   - `preview` : 배포 했을 때 미리보기
 - `dependencies` : 필요한 패키지를 정의
   - 버전 표기법
     - `틸드(~)` : 작성된 버전보다 높거나 같고, 다음 마이너 버전보다 낮은 버전 내에서 자동으로 업데이트
       - ex) `~3.3.4` => `>=3.3.4` and `<3.4.0`
     - `캐럿(^)` : 작성된 버전보다 높거나 같고, 다음 메이저 버전보다 낮은 버전 내에서 자동으로 업데이트
       - ex) `^3.3.4` => `>=3.3.4` and `<4.0.0`
       - 호환성을 유지하는 버전 중 가장 최신 버전으로 업데이트(많이 사용됨)
 - `devDependencies` : 개발 환경에서 필요한 패키지를 정의

### package-lock.json

 - `$ npm install` 실행 시 자동으로 생성되는 파일
 - 현재 프로젝트에서 사용 중인 패키지들과 버전 정보를 모두 포함
 - 완벽한 패키지 설치를 보장하기 위해서 사용됨
   - 패키지 간 의존성 관리를 자동으로 처리해줌
   - pip 의 requirements.txt 역할
 - 다른 환경에서 동일한 환경을 구성하기 위해서
   - 공유 시 두 파일을 모두 주어야 한다.
   - 공유 받은 파일들의 `name`, `version`은 상황에 맞게 수정

 - `npm install` 의 동작 과정
 1. `package.json` 파일 검사
    - 설치가 필요한 패키지 목록 확인
 2. `package.json` 파일 검사
    - 의존성 패키지 목록 확인 후 설치

 - `resolved` : 해당 패키지의 다운로드 경로
 - `integrity` : 다운로드 받은 패키지의 무결성을 체크하는 해시값
   - 정확한 패키지를 다운로드 받았는지 확인
   - 무결성 체크 실패 시 다운로드를 중지
   - 보안, 일관성 등 관리하기 위해 매우 중요한 옵션
 - `dev` : 개발 버전의 의존성으로 설치되었는 지 여부(true/false)
 - `bin` : 전역적으로 실행가능한 설치 경로
 - `engines` : 해당 패키지를 사용하기 위해 필요한 Node.js, npm 버전을 명시
 - `optionalDependencies` : 선택적인 의존성을 가진 패키지

## Component

 - 재사용 가능한 코드 블록
 - UI를 독립적이고 재사용 가능한 일부분으로 분할하고 각 부분을 개별적으로 다룰 수 있음
 - 자연스럽게 앱은 중첩된 Componentd의 트리로 구성됨

## SFC build tool

 - Node Package Manager(NPM) : Node.js의 기본 패키지 관리자
  
### public 디렉토리

 - 주로 다음 정적 파일을 위치 시킴

### src 디렉토리

 - 프로젝트의 주요 소스 코드를 포함하는 곳
 - 컴포넌트, 스타일, 라우팅 등 프로젝트의 핵심 코드를 관리

### src/assets

 - 프로젝트 내에서 사용되는 자원(이미지, 폰트, 시트 등)을 관리
 - 컴포넌트 자체에서 참조하는 내부 파일을 저장하는데 사용
 - 컴포넌트가 아닌 곳에서는 public 디렉토리에 위치한 파일을 사용

### src/components

 - Vue 컴포넌트들을 작성하는 곳

### src/App.vue

 - Vue 앱의 최상위 Root 컴포넌트
 - 다른 하위 컴포넌트들을 포함
 - 애플리케이션 전체의 레이아웃과 공통적인 요소를 정의

### src/main.js

 - Vue 인스턴스를 생성하고, 애플리케이션을 초기화하는 역할
 - 필요한 라이브러리를 import 하고 전역 설정을 수행

### index.html

 - Vue 앱의 기본 HTML 파일
 - 앱의 진입점 (entry point)
 - Root 컴포넌트인 App.vue가 해당 페이지에마운트(mount)됨
 - 필요한 스타일 시트, 스크립트 등의 외부 리소스를 로드 할 수 있음

## 모듈과 번들러

### Module : 프로그램을 구성하는 독립적인 코드 블록 (*.js 파일)

 - 개발하는 애플리케이션의 크기가 커지고 복잡해지면서 파일 하나에 모든 기능을 담기가 어려워짐
 - 자연스럽게 파일을 여러 개로 분리하여 관리를 하게 되었고, 이때 분리된 파일이 각각 모듈이 됨
 - 모듈 수가 많아지고 라이브러리 혹은 모듈 간의 의존성이 깊어지며 특정한 곳에서 발생한 문제가 어떤 모듈 간의 문제인지 파악하기 어려워 짐

### Bundler

 - 여러 모듈과 파일을 하나의 번들로 묶어 최적화하여 애플리케이션에서 사용할 수 있게 만들어주는 도구
 - 의존성 관리, 코드 최적화, 리소스 관리 등
 - Bundler가 하는 작업을 Bunding이라 함
 - Vite는 Rollup이라는 Bundler를 사용하며 개발자가 별도로 기타 환경설정에 신경 쓰지 않도록 모두 설정해두고 있음


## Virtual DOM

 - 가상의 DOM을 메모리에 저장하고 실제 DOM과 동기화하는 프로그래밍 개념
 - 실제 DOM과 변경 사항 비교를 통해 변경된 부분만 실제 DOM에 적용하는 방식
 - 웹 애플리케이션 성능 향상을 위한 Vue의 내부 렌더링 기술

 - 장점
   - 

 - 단점


### Virtual DOM 주의사항

 - 실제 DOM에 직접 접근하지 말 것
   - JS에 사용하는 DOM 접근 메서드 사용 금지
   - querySelector, createElement, addEventListener