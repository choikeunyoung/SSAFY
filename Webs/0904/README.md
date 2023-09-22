# 웹 구조화

## HTML ( Hyper Text Markup Language )

 - 웹 페이지의 의미와 구조를 정의하는 언어

 ```HTML
    <!-- 해당 문서가 html로 문서라는 것을 나타냄 -->
    <!DOCTYPE html> 
    <!-- 전체 페이지의 콘텐츠를 포함 -->
    <html lang="en">
    <!-- HTML 문서에 관련된 설명, 설정 등 사용자에게 보이지 않음 -->
    <head>
        <!-- 한글 깨지는거 방지 -->
        <meta charset="UTF-8">
        <!-- 키워드, 설명, 제작자 등... -->
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- 브라우저 탭 및 즐겨찾기 사용시 표시되는 제목 -->
        <title>My page</title>
    </head>
    <!-- 페이지에 표시되는 모든 콘텐츠 -->
    <body>
        <p>This is my page</p>
    </body>
    </html>
 ```

 ```HTML
    <p>My cat is very grumpy</p>
<!--여는 태그/     내용   /닫는 태그 -->
<!--           요소            -->
 ```
 - 하나의 요소는 여는 태그, 닫는 태그, 그 안의 내용들로 구성됨
 - 닫는 태그가 없는 태그도 존재함

### HTML Attributes(속성)

```HTML
    <p class="editor-note">My cat is very grumpy</p>
```

 - 규칙
   - 속성은 요소 이름과 속성 사이에 공백이 있어야 함
   - 하나 이상의 속성들이 있는 경우 속성 사이에 공백으로 구분함
   - 속성 값은 열고 닫는 따옴표로 감싸야 함

 - 목적
   - 나타내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
   - CSS에서 해당 요소를 선택하기 위한 값으로 활용됨

```HTML
    <h1>Heading</h1>
```

 - h1 요소는 텍스트 크기를 키우는 것이 아닌 문서의 최상위 제목이라는 의미를 부여
 - 대표적인 HTML Text structure
```
 - Heading & Paragraphs : h1 ~ 6, p
 - Lists : ol, ul, li
 - Emphasis & Importance : em, strong
```

## CSS ( Cascading Style Sheet )

 - 웹 페이지의 디자인과 레이아웃을 구성하는 언어

```CSS
/* 선택자 */
    h1 {
    /* 속성: 값 */
        color: red;
        font-size: 30px;
    }
```

### CSS 적용 방법

 1. 인라인(Inline) 스타일

    - HTML 요소 안에 style 속성 값으로 작성

```HTML
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>My page</title>
    </head>
    <body>
        <h1 style="color: blue; background-color: yellow;">Hello World!</h1>
    </body>
    </html>
```

 2. 내부(Internal) 스타일 시트

    - head 태그 안에 style 태그에 작성

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My page</title>
    <style>
        h1 {
            color: blue;
            background-color: yellow;
        }
    </style>
</head>
</html>
```

 3. 외부(External) 스타일 시트
 
    - 별도의 CSS 파일 생성 후 HTML link 태그를 사용해 불러오기

```HTML
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="style.css">
        <title>My page</title>
    </head>
    <body>
        <p>This is my page</p>
        <a href="style.css"></a>
    </body>
    </html>
```
```CSS
    /* style.css */
    h1 {
        color: blue;
        background-color: yellow;
    }
```

### CSS Selectors 특징

 - 전체 선택자(*) : HTML 모든 요소를 선택
 - 요소 선택자(tag) : 지정한 모든 태그를 선택
 - 클래스 선택자(class) ("."(dot)) : 주어진 클래스 속성을 가진 모든 요소를 선택
 - 아이디 선택자(id) ("#") : 주어진 아이디 속성을 가진 요소 선택 ( 한 아이디 요소만을 권장 )
 - 속성(attr) 선택자
 - 자손 결합자 (" " (space))
   - 첫 번째 요소의 자손 요소들 선택
   - p span 은 <p> 안에 모든 <span> 선택
 - 자식 결합자 (">")

### Specificity ( 우선순위 )

 - 동일한 요소에 적용 가능한 같은 스타일을 두 가지 이상 작성 시 어떤 규칙이 적용될지 정하는 것
 - Cascade(계단식) : 동일한 우선순위를 같는 규칙이 적용될 때 CSS에 마지막에 나오는 규칙이 적용됨

```CSS
/* Cascade 예시 */
/* h1 태그 내용의 색은 순서대로 맨 마지막에 나온 purple 적용된다. */
    h1 {
        color: red;
    }

    h1 {
        color: purple;
    }

/* Specificity 예시 */
/* 동일한 h1 태그에 요소 선택자와 클래스 선택자가 적용되면 purple이 적용된다. */
    .make-red {
        color: red;
    }

    h1 {
        color: purple;
    }
```

 1. Importance : !important
 2. Inline 스타일
 3. 선택자 : Id 선택자 > class 선택자 > 요소 선택자
 4. 소스 코드 순서


### CSS 상속
 
 - 기본적으로 CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속해 재사용성을 높였다.

```html
 - 상속 되는 속성
    - Text 관련 요소(font, color, text-align), opacity, visibility 등
 - 상속 되지 않는 속성
    - Box model 관련 요소 (width, height, border, box-sizing ...)
    - position 관련 요소 (position, top/right/bottom/left, z-index) 등
```