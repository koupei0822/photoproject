from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#URLパターンを逆引きできるように名前を付ける
app_name = "accounts"

#URLパターンを登録するための変数
urlpatterns = [
    #サインアップページのビューの呼び出し
    #「http(s)://<ホスト名>/signup/」へのアクセスに対して、
    #viewsモジュールのSignUpViewをインスタンス化する
    path("signup/",views.SignUpView.as_view(),name="signup"),

    #サインアップページのビューの呼び出し
    #「http(s)://<ホスト名>/signup_syccess/」へのアクセスに対して、
    #viewsモジュールのSignUpSuccessViewをインスタンス化する
    path("signup_success/",views.SignUpSuccessView.as_view(),name="signup_success"),

    #ログインページの表示
    #django.contrib.auth.views.LoginViewをインスタンス化してログインページを表示する
    path("login/",auth_views.LoginView.as_view(template_name="login.html"),name="login"),

    #ログアウトを実行
    #django.contrib.auth.views.LogoutViewをインスタンス化して老ぐアウトさせる
    path("logout/",auth_views.LogoutView.as_view(template_name="logout.html"),name="logout"),
]