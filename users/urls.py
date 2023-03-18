from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings
app_name = 'user'

urlpatterns = [
    path("login", views.login_view, name = 'login'), # login path 설정
    path("logout", views.logout_view, name = 'logout'), # logout path 설정
    path("signup", views.signup_view, name = 'signup'), # signup path 설정
    path("login/Nagoya", views.GetNagoya, name = 'Nagoya'), # l
    path("login/Takayama", views.GetTakayama, name = 'Takayama'), # l
    path("login/Toyama", views.GetToyama, name = 'Toyama'), # 
    path("login/Gero", views.GetGero, name = 'Gero'), # 
    path("login", views.GetBacktoLogin, name = 'GetBacktoLogin'), # 
]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)