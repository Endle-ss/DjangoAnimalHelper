from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cards/', views.cards, name='cards'),  # Маршрут для /cards
    path('search/', views.search_cards, name='search_cards'),
    path('card/<int:card_id>/', views.card_detail, name='card_detail'),
]