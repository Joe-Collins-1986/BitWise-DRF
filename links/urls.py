from django.urls import path
from links import views

urlpatterns = [
    path('', views.LinkList.as_view()),
    path('<int:pk>/', views.LinkDetail.as_view()),
]
