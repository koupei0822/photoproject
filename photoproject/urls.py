
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    #photo.urlsへのURLパターン
    path("",include("photo.urls")),

    #account("",include("accounts.urls")),
    path("",include("accounts.urls")),

    #パスワードリセットのためのURLパターン
    #PasswordResetConfirmViewがプロジェクトのurls.pyを参照するのでここに記載
    #パスワードリセット申込ページ
    path("password_reset/",
        auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
        name="password_reset"),
    #メール送信完了ページ
    path("password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="password_reset_sent.html"),
            name="password_reset_done"),

    #パスワードリセットページ
    path("reset/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password_reset_form.html"),
        name="password_reset_confirm"),

    #パスワードリセット完了ページ
    path("reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password_reset_done.html"),
        name="password_reset_complete"),
]
