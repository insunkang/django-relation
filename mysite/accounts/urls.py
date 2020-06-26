from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('delete/', views.delete, name="delete"),
    path('update/', views.update, name="update"),
    path('password/',views.password, name="password"),
    path('follow/<int:user_pk>/',views.follow,name="follow"),
    #상단으로 가면 accounts뒤에오는 모든 문자열이 다 적용된다 그래서 맨 밑
    path('<str:username>/',views.profile,name="profile"), 

    

]