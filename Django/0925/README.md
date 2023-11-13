# Django ORM with view

 1. Read
 2. Create
 3. HTTP request methods
 4. Delete
 5. Update

## Read

 1. 전체 게시글 조회

 ```python
    # articles/views.py
    from .models import Article

    def index(request):
        articles = Article.objects.all()
        context = {
            "articles" : articles,
        }
        return render(request, "articles/index.html", context)
 ```
 ```HTML
    <!-- articles/index.html -->
    <h1>Articles</h1>
    <hr>
    {% for article in articles %}
        <p>글 번호: {{ article.pk }}</p>
        <p>글 제목: {{ article.title }}</p>
        <p>글 내용: {{ article.content }}</p>
        <hr>
    {% endfor %}
 ```

 2. 단일 게시글 조회

 ```python
    # articles/urls.py
    urlpatterns = [
        ...
        path("<int:pk>/", views.detail, name="detail"),
    ]

    # articles/views.py

    def detail(request, pk):
        article = Article.objects.get(pk=pk)
        context = {
            "article" : article,
        }
        return render(request, "articles/detail.html", context)
 ```
 ```HTML
    <h2>DETAIL</h2>
    <h3>{{ article.pk }} 번째 글</h3>
    <hr>
    <p>제목: {{ article.title }}</p>
    <p>내용: {{ article.content }}</p>
    <p>작성일: {{ article.created_at }}</p>
    <p>수정일: {{ article.updated_at }}</p>
    <hr>
    <a href="{% url 'articles:index' %}">[back]</a>
 ```

## Create

 - 구현하기 위한 view 함수는 2개가 필요하다.
 - 사용자 입력 데이터를 받을 페이지를 렌더링
 - 사용자가 입력한 데이터를 받아 DB에 저장

 #### new 기능 구현

 ```python
    # articles/urls.py

    urlpatterns = [
        ...
        path("new/", views.new, name="new"),
    ]

    # articles/views.py
    def new(request):
        return render(request, "articles/new.html")
 ```
 ```HTML
    <!-- templates/articles/new.html -->
    <h1>NEW</h1>
    <form action="#" method="GET">
        <div>
            <label for="title">Title: </label>
            <input type="text" name="title" id="title">
        </div>
        <div>
            <label for="content">Content: </label>
            <textarea name="content" id="content"></textarea>
        </div>
        <input type="submit">
    </form>
    <hr>
    <a href="{% url 'articles:index' %}">[back]</a>
 ```

 #### create 기능 구현

 ```python
    # articles/urls.py

    urlpatterns = [
        ...
        path("create/", views.create, name="create"),
    ]

    # articles/views.py
    def create(request):
        title = request.GET.get("title")
        content = request.GET.get("content")
        # 1.
        # article = Article()
        # article.title = title
        # article.content = content
        # article.save()

        # 2.
        article = Article(title=title, content=content)
        article.save()

        # 3.
        # Article.objects.create(title=title, content=content)
        return render(request, "articles/create.html")
 ```
 ```HTML
    <!-- templates/articles/create.html -->
    <h1>게시글이 작성 되었습니다.</h1>

    <!-- templates/articles/new.hmtl -->
        <h1>NEW</h1>
    <form action="{% url 'articles:creat' %}" method="GET">
 ```

## HTTP request methods

 - HTTP : 네트워크 상에서 데이터를 주고 받기위한 약속
 - HTTP request methods : 데이터에 어떤 요청을 원하는지를 나타내는 것( GET & POST )
 - "GET" Method : 특정 리소스를 조회하는 요청 (GET으로 데이터를 전달하면 Query String 형식으로 보내짐)
 - "POST" Method : 특정 리소스에 변경(생성, 수정, 삭제)을 요구하는 요청 (POST로 데이터를 전달하면 HTTP Body에 담겨 보내짐)