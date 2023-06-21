"""
bitwise URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from .views import logout_route

urlpatterns = [
    path('', include_docs_urls(title="BitWise Documentation")),
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),

    path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path(
        'dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
    ),

    path('profiles/', include('profiles.urls')),
    path('languages/', include('languages.urls')),
    path('articles/', include('articles.urls')),
    path('comments/', include('comments.urls')),
    path('likes/', include('likes.urls')),
    path('followers/', include('followers.urls')),
    path('recomendations/', include('recommended.urls')),
    path('links/', include('links.urls')),

]
