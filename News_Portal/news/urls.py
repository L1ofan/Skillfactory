from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, NewsSearch, PostDetail, PostCreate, PostUpdate, PostDelete


urlpatterns = [
   path('news/', PostsList.as_view()),
   path('news/<int:pk>/', PostDetail.as_view(), name='Post'),
   path('news/create/', PostCreate.as_view(), name='Post_create'),
   path('news/search/', NewsSearch.as_view(), name='Posts_search'),
   path('news/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('articles/create/', PostCreate.as_view(), name='articles_create'),
   path('articles/<int:pk>/update/', PostUpdate.as_view(), name='articles_update'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),
]

