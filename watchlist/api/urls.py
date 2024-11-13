from django.urls import path
from watchlist.api.views import MovieList, MovieDetail
# from watchlist.api.views import movie_list, movie_detail

urlpatterns = [
    path('list/', MovieList.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
]
