# Django Template System

 - 데이터 표현을 제어하면서, 표현과 관련된 부분을 담당
 - HTML의 콘텐츠를 변수 값에 따라 바꾸고 싶을 경우

```python
    def index(request):
        context = {
            "name" : "Jane",
        }
        return render(request, "articles/index.html", context)
```
```html
    <body>
        <h1>Hello, {{ name }}</h1>
    </body>
```

## Django Template Language

 - Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템

 **1. Variable {{ variable }}**

 - render 함수의 세번째 인자로 딕셔너리 데이터를 사용
 - 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
 - dot(.)를 사용하여 변수 속성에 접근할 수 있음

 **2. Filters {{ variable|filter }}**

 - 표시할 변수를 수정할 때 사용
 - chained가 가능하며 일부 필터는 인자를 받기도 함
 - 약 60개의 built-in template filters를 제공

 **3. Tags {% tag %}**

 - 반복 또는 논리를 수행하여 제어 흐름을 만듦
 - 일부 태그는 시작과 종료 태그가 필요
 - 약 24개의 built-in template tags를 제공

 **4. Comments**

 - {# #} // {% comment %} {% endcomment %}

```django
    {% comment %}
        {% if name == "Sophia" %}
        {% endif %}
    {% endcomment %}
```