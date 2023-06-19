from django.urls import path
from recommended import views

urlpatterns = [
    path('add/', views.RecommendArticle.as_view()),
    path('', views.ReceivedRecommendationsList.as_view()),
    path('remove/<int:pk>/',
         views.DeleteRecommendation.as_view()),
]
