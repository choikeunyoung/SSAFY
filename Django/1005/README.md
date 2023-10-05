# Django Authentication System 2

 1. 회원 가입
 2. 회원 탈퇴
 3. 회원정보 수정
 4. 비밀번호 변경
 5. 로그인 사용자에 대한 접근 제한

## 회원가입 

 - User 객체를 Create 하는 과정
 - UserCreationForm() : 회원 가입시 사용자 입력 데이터를 받을 built-in ModelForm

 ```python
    # accounts/urls.py
    
    app_name = "accounts"
    urlpatterns = [
        path('signup/', views.signup name='singup'),
    ]

    # accounts/views.py

    from django.contrib.auth.forms import UserCreationForm

    def signup(request):
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("aricles:index")
        else:
            form = UserCreationForm()
        context = {
            'form' : form,
        }
        return render(request, "accounts/signup.html", context)
 ```
 ```Django
    <!-- accounts/signup.html -->

    <h1>회원가입</h1>
    <form action="{% url 'accounts:signup' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>
 ```

 - 위와 같이 로직구현하면 에러 페이지가 발생한다.
 - UserCreationfForm이 우리가 대체한 커스텀 유저 모델이 아닌 기존 유저 모델로 작성된 클래스이기 때문
 - UserCreationForm / UserChangeForm 두 Form 모두 class Meta: model = User 가 작성됨

 ```python
    # accounts/forms.py

    from django.contrib.auth import get_user_model
    from django.contrib.auth.forms import UserCreationForm, UserChangeForm

    class CustomUserCreationForm(UserCreationForm):
        class Meta(UserCreationForm.Meta):
            model = get_user_model()
            
    class CustomUserChangeForm(UserChangeForm):
        class Meta(UserChangeForm.Meta):
            model = get_user_model()
 ```
 
 - get_user_model() : 현재 프로젝트에서 활성화된 사용자 모델(active user model)을 반환하는 함수

### User 모델을 직접 참조하지 않는 이유

 - get_user_mdoel()을 사용해 User 모델을 참조하면 커스텀 User 모델을 자동으로 반환해주기 때문
 - Django는 User 클래스를 직접 참조하는 대신 get_user_model()을 사용해 참조해야 한다고 필수적으로 강조하고 있음

## 회원 탈퇴

 - User 객체를 Delete 하는 과정

 ```python
    # accounts/urls.py

    app_name = "accounts"
    urlpatterns = [
        path("delete/", views.delete, name="delete"),
    ]

    # accounts/views.py
    
    def delete(request):
        request.user.delete()
        return redirect("articles:index")
 ```
 ```Django
    <!-- accounts/index.html -->
    <form action="{% url 'accounts:delete' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="회원탈퇴">
    </form>
 ```

## 회원정보 수정

 - User 객체를 Update 하는 과정
 - UserChangeForm() : 회원정보 수정 시 사용자 입력 데이터를 받을 built-in ModelForm

 ```python
    # accounts/urls.py

    app_name = "accounts"
    urlpatterns = [
        path('update/', views.update, name="update"),
    ]

    # accounts/views.py
    from .forms import CustomUserChangeForm

    def update(request):
        if request.method == "POST":
            pass
        else:
            form = CustomUserChangeForm(instance=request.user)
        context = {
            "form" : form,
        }
        return render(request, 'accounts/update.html', context)
 ```
 ```HTML
    <!-- accounts/update.html -->
    <h1>회원정보 수정</h1>
    <form action="{% url 'accounts:update' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>
 ```

### UserChangeForm 사용 시 문제점

 - User 모델의 모든 정보(fields)까지 모두 출력되어 수정이 가능하기 때문에 일반 사용자들이 접근해서는 안되는 정보를 출력하지 않도록 해야 함

### CustomUserChangeForm 출력 필드 재정의

 - User Model의 필드 목록 확인

 ```python
    # accounts/forms.py

    class CustomUserChangeForm(UserChangeForm):

        class Meta(UserChangeForm.Meta):
            model = get_user_model()
            fields = ('first_name', 'last_name', 'email',)
 ```

## 비밀번호 변경

 - 인증된 사용자의 Session 데이터를 Update 하는 과정
 - PasswordChangeForm() : 비밀번호 변경 시 사용자 입력 데이터를 받을 built-in Form

 ```python
    # crud/urls.py
    from accounts import views

    urlpatterns = [
        path('<int:user_pk>/password/', views.change_password, name="change_password"),
    ]

    # accounts/views.py
    from django.contrib.auth.forms import PasswordChangeForm

    def change_password(request, user_pk):
        if request.method == "POST":
            pass
        else:
            form = PasswordChangeForm(request.user)
        context = {
            'form' : form,
        }
        return render(request, 'accounts/change_password.html', context)
 ```
 ```Django
    <!-- accounts/change_password.html -->

    <h1>비밀번호 변경</h1>
    <form action="{% url 'change_password' user.pk %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>
 ```

## 세션 무효화 방지하기

 - 암호 변경 시 세션 무효화
 - 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게 되어 버려 로그인 상태가 유지되지 못하고 로그아웃 처리
 - 비밀번호가 변경되면서 기존 세션과의 회원 인증 정보가 일치하지 않기 때문

 - update_session_auth_hash(request, user) : 암호 변경 시 세션 무효화를 막아주는 함수

 ```python
    # accounts/views.py
    from django.contrib.auth import update_session_auth_hash

    def change_password(request):
        if request.method == "POST":
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                return redirect("articles:index")
        else:
            form = PasswordChangeForm(request.user)
        context = {
            'form' : form,
        }
        return render(request, 'accounts/change_password.html', context)
 ```

## 인증된 사용자에 대한 접근 제한

 1. is_authenticated : 사용자가 인증 되었는지 여부를 알 수 있는 User model의 속성 (True or False)
 2. login_required 데코레이터 : 인증된 사용자에 대해서만 view 함수를 실행시키는 데코레이터 (비인증 사용자의 경우 /accounts/login/ 주소로 redirect 시킴)