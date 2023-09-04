# 웹 구조화

## HTML ( Hyper Text Markup Language )

 - 웹 페이지의 의미와 구조를 정의하는 언어

 ```HTML
    <!-- 해당 문서가 html로 문서라는 것을 나타냄 -->
    <!DOCTYPE html> 
    <html lang="en">
    <!-- HTML 문서에 관련된 설명, 설정 등 사용자에게 보이지 않음 -->
    <head>
        <!-- 한글 깨지는거 방지 -->
        <meta charset="UTF-8">
        <!-- 키워드, 설명, 제작자 등... -->
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My page</title>
    </head>
    <!-- 페이지에 표시되는 모든 콘텐츠 -->
    <body>
        <p>This is my page</p>
    </body>
    </html>
 ```

### HTML Attributes(속성)

```html
    <p class="editor-note">My cat is very grumpy</p>
```

 - 규칙
   - 속성은 요소 이름과 속성 사이에 공백이 있어야 함
   - 하나 이상의 속성들이 있는 경우 속성 사이에 공백으로 구분함
   - 속성 값은 열고 닫는 따옴표로 감싸야 함

 - 목적
   - 나타내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
   - CSS에서 해당 요소를 선택하기 위한 값으로 활용됨

```html
    <h1>Heading</h1>
```

 - h1 요소는 텍스트 크기를 키우는 것이 아닌 문서의 최상위 제목이라는 의미를 부여


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
    - HTML 요소 안에
 2. 내부(Internal) 스타일 시트
    - head 태그 안에 style 태그에 작성

```HTML
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My page</title>
    <style>

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
        <title>My page</title>
    </head>
    <body>
        <p>This is my page</p>
        <a href=""></a>
    </body>
    </html>
```

### CSS Selectors 특징

 - 전체 선택자 (*) : HTML 모든 요소를 선택
 - 요소 선택자 : 지정한 모든 태그를 선택
 - 클래스 선택자 ("."(dot)) : 주어진 클래스 속성을 가진 모든 요소를 선택
 - 아이디 선택자 ("#")
 - 자손 결합자 (" " (space))
   - 첫 번째 요소의 자손 요소들 선택
   - p span 은 <p> 안에 모든 <span> 선택
 - 자식 결합자 (">")


### Specificity ( 우선순위 )

 - Cascade(계단식) : 동일한 우선순위를 같는 규칙이 적용될 때 CSS에 마지막에 나오는 규칙이 적용됨

 1. Importance : !important
 2. Inline 스타일
 3. 선택자 : Id 선택자 > class 선택자 > 요소 선택자
 4. 소스 코드 순서