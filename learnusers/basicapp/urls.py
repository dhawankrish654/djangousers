from django.urls import path
from django.conf.urls import url,include
from basicapp import views

app_name='basicapp'




urlpatterns = [
path('register',views.register,name='register'),
path('user_login',views.user_login,name='user_login'),
]
