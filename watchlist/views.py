# from django.shortcuts import render
# from watchlist.models import Movie
# from django.http import JsonResponse

# # Create your views here.
# def movie_list(request):
#     movies = Movie.objects.all()
#     context = {
#         'movie_list': list(movies.values())
#     }
#     return JsonResponse(context)


# def movie_detail(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     context = {
#         'name': movie.name,
#         'description': movie.description
#     }
#     return JsonResponse(context)