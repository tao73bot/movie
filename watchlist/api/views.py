from watchlist.models import Movie
from . serializers import MovieSerializer
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView # Class Based Views
from rest_framework import status


###### Function Based Views ######
# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#     else:
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def movie_detail(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = MovieSerializer(instance=movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


###### Class Based Views ######
class MovieList(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serilizer = MovieSerializer(movies, many=True)
        return Response(serilizer.data)

    def post(self, request):
        serilizer = MovieSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetail(APIView):
    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serilizer = MovieSerializer(movie)
        return Response(serilizer.data)

    def put(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serilizer = MovieSerializer(instance=movie, data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        else:
            return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)