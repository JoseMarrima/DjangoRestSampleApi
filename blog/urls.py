from django.urls import path
from blog import views
from rest_framework.urlpatterns import format_suffix_patterns

# Class based urls
urlpatterns = [
    path('article/', views.ArticleList.as_view()),
    path('article/<int:pk>/', views.ArticleDetail.as_view()),
]

# # Function based urls
# urlpatterns = [
#     path('article/', views.article_list),
#     path('article/<int:pk>/', views.article_detail),
# ]

urlpatterns = format_suffix_patterns(urlpatterns)