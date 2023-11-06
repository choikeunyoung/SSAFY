# Django REST framework

 1. DRF with N:1 Relation
 2. 역참조 데이터 구성
 3. API 문서화

## DRF with N:1 Relation

 - Comment 모델 정의
 ```python
    # articles/models.py

    class Comment(models.Model):
        article = models.ForeignKey(Article, on_delete=models.CASECADE)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
 ```

### GET

 - 댓글 목록 조회를 위한 CommentSerializer 정의
 ```python
    # articles/serializers.py
    from .models import Article, Comment

    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = "__all__"

    urlpatterns = [
        path('comments/', views.comment_list),
    ]

    # articles/views.py
    from .models import Article, Comment
    from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

    @api_view(['GET'])
    def comment_list(request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
 ```

### GET- Detail

 - 단일 댓글 조회
 ```python
    # articles/urls.py

    urlpatterns = [
        path('comments/<int:comment_pk>/', views.comment_detail),
    ]

    # articles/views.py

    @api_views(['GET'])
    def comment_detail(request, comment_pk):
        comment = Comment.objects.get(pk=comment_pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
 ```

### POST

 - 단일 댓글 생성을 위한 url 및 view 함수 작성
 ```python
    # articles/urls.py
    urlpatterns = [
        path('articles/<int:article_pk>/comments/', views.comment_create),
    ]

    # articles/views.py
    @api_View(["POST"])
    def comment_create(request, article_pk):
        article = Article.objects.get(pk=article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
 ```

 - serializer 인스턴스의 save() 메서드는 특정 Serializer 인스턴스를 저장하는 과정에서 추가 데이터를 받을 수 있음

 ```python
    # articles/views.py
    @api_View(["POST"])
    def comment_create(request, article_pk):
        article = Article.objects.get(pk=article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article = article) # 이 부분에서 추가로 데이터 받음
            return Response(serializer.data, status=status.HTTP_201_CREATED)
 ```

### 읽기 전용 필드

 - 데이터 전송하는 시점에 "유효성 검사에서 제외시키고, 데이터 조회 시에는 출력" 하는 필드
 ```python
    # articles/serializers.py

    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = "__all__"
            read_only_fields = ("article", )
 ```

### DELETE & PUT

 - 단일 댓글 삭제 및 수정을 위한 view 함수 작성
 ```python
    # articles/views.py
    @api_view(['GET', 'DELETE', 'PUT'])
    def comment_detail(request, comment_pk):
        comment = Comment.objects.get(pk=comment_pk)
        if request.method == "GET":
            serializer = CommentSErializer(comment)
            return Response(serializer.data)
        
        elif request.method == "DELETE":
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        elif request.method == "PUT":
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
 ```

### 응답 데이터 재구성

 - 필요한 데이터를 만들기 위해 Serializer 내부에 추가 선언 가능
 ```python
    # articles/serializers.py
    class CommentSerializer(serializers.ModelSerializer):
        class ArticlesTitleSerializer(serializers.ModelSerializer):
            class Meta:
                model = Article
                fields = ('title', )
        article = ArticlesTitleSerializer(read_only=True)

        class Meta:
            model = Comment
            fields = "__all__"
 ```

### 역참조 데이터 구성

 - Article => Comment 간 역참조 관계를 활용한 JSON 데이터 재구성
   1. 단일 게시글 조회 시 해당 게시글 작성된 댓글 목록 데이터도 함께 붙여서 응답
    ```python
        class CommentSerializer(serializers.ModelSerializer):
            class Meta:
                model = Comment
                fields = "__all__"
                read_only_fields = ("article", )

        class ArticleSerializer(serializers.ModelSerializer):
            comment_set = CommentSerializer(many=True, read_only=True)
            
            class Meta:
                model = Article
                fields = "__all__"
    ```

   2. 단일 게시글 조회 시 해당 게시글에 작성된 댓글 개수 데이터도 함꼐 붙여서 응답
    ```python
        # articles/serializers.py

        class ArticleSerializer(serializers.ModelSerializer):
            comment_set = CommentSerializer(many=True, read_only=True)
            comment_count = serializer.IntegerField(source='comment_set.count', read_only=True)
            
            class Meta:
                model = Article
                fields = "__all__"
    ```

    - 'source'
      - 필드를 채우는 데 사용할 속성의 이름
      - 점 표기법을 사용하여 속성을 탐색 할 수 있음
    ```python
        # articles/serializers.py

        class ArticleSerializer(serializers.ModelSerializer):
            comment_set = CommentSerializer(many=True, read_only=True)
            comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

            class Meta:
                model = Article
                fields = '__all__'
    ```

### 읽기 전용 필드 지정 이슈

 - 특정 필드를 override 혹은 추가한 경우 read_only_fields는 동작하지 않음
 - 해당 필드의 read_only 키워드 인자로 작성해야 함
 ```python
    class ArticleSerializer(serializers.ModelSerializer):
        comment_set = CommentSerializer(many=True)
        comment_count = serializers.IntegerField(source='comment_set.count')

        class Meta:
            model = Article
            fields = '__all__'
            read_only_fields = ('comment_set', 'comment_count', )
 ```

## OpenAPI Specification

 - RESTful API를 설명하고 시각화하는 표준화된 방법
 - DRF 위한 OpenAPI 3.0 구조 생성을 도와주는 라이브러리
 ```python
    # settings.py
    INSTALLED_APPS = [
        'drf_spectacular',
    ]

    REST_FRAMEWORK = {
        'DEFAULT_SCHEMA_CLASS' : 'drf_spectacular.openapi.AutoSchema',
    }

    # drf/urls.py
    from drf_spectacular.views import SpectacularAPIView, SpectacuarRedocView, SpectacularSwaggerView

    urlpatterns = [
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
        path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    ]
 ```

 - OAS의 핵심 이점
   - API 먼저 설계하고 명세를 작성한 후, 이를 기반으로 코드를 구현하는 방식
   - API의 일관성을 유지하고, API 사용자는 더 쉽게 API를 이해하고 사용할 수 있음
   - OAS를 사용하면 API가 어떻게 작동하는지를 시각적으로 보여주는 문서를 생성할 수 있으며, 이는 API를 이해하고 테스트하는 데 매우 유용
   - 이런 목적으로 사용되는 도구가 Swagger-UI or ReDoc

## Django shortcuts functions

 - get_object_or_404() : 모델 manager objects에서 get()을 호출하지만, 해당 객체가 없을 땐 기존 DoesNotExist 예외 대신 Http404를 raise 함
 ```python
    # articles/views.py

    from django.shortcuts import get_object_or_404

    article = Article.objects.get(pk=article_pk)
    comment = Comment.objects.get(pk=comment_pk)

    # 위 코드를 모두 다음과 같이 변경

    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
 ```

 - get_list_or_404() : 모델 manager objects에서 filter()의 결과를 반환하고, 해당 객체 목록이 없을 땐 Http404를 raise 함
 ```python
    # articles/views.py

    from django.shortcuts import get_object_or_404, get_list_or_404

    articles = Article.objects.all()
    comments = Comment.objects.all()
    
    # 위 코드를 모두 다음과 같이 변경
    articles = get_list_or_404(Article)
    comment = get_list_or_404(Comment)
 ```

 - 클라이언트에게 "서버에 오류가 발생하여 요청을 수행할 수 없다(500)"라는 원인이 정확하지 않은 에러를 제공하기 보다는, 적절한 예외 처리를 통해 클라이언트에게 보다 정확한 에러 현황을 전달하는 것도 매우 중요한 개발 요소 중 하나이기 떄문