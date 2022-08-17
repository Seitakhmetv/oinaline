from django.contrib import admin
from django.urls import path
from api.views import platform_list, get_platform, PublisherListAPIVIEW, GetPublisherAPIVIEW, GenreList, GetGenreAPIVIEW, TypeList, GameList, ScreenshotList, GetGameAPIVIEW, GetScreenshotAPIVIEW, GetTypeAPIVIEW
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),

    path('platforms/', platform_list),
    path('platforms/<int:id>/', get_platform),
    
    path('publishers/', PublisherListAPIVIEW.as_view()),
    path('publishers/<int:pk>/', GetPublisherAPIVIEW.as_view()),
    
    path('genres/', GenreList.as_view()),
    path('genres/<int:id>/', GetGenreAPIVIEW.as_view()),
    
    path('screenshots/', ScreenshotList.as_view()),
    path('screenshot/<int:id>/', GetScreenshotAPIVIEW.as_view()),
    
    path('games/', GameList.as_view()),
    path('games/<int:id>/', GetGameAPIVIEW.as_view()),

    path('types/', TypeList.as_view()),
    path('types/<int:id>/', GetTypeAPIVIEW.as_view()),

    
]
