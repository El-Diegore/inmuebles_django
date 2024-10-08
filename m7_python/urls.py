from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.indexView, name='home'),
    path('login/', LoginView.as_view(next_page='dashboard'), name='login_url'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.registerView, name='register_url'),
    path('register_tipo/', views.register_tipoView, name='register_tipo_url'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('update_profile/', views.profile, name='update_profile'),
]