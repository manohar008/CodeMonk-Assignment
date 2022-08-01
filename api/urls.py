from django.urls import path
from .views import RegisterView, LoginView, WordSearch

urlpatterns = [
        path('register/', RegisterView.as_view(), name="register"),
        path('login/', LoginView.as_view(), name="login"),
        path('word_search/', WordSearch.as_view(), name="word_search")
        ]
