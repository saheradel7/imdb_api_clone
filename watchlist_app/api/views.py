from watchlist_app.models import Movie
from rest_framework.decorators import api_view
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status


@api_view(["GET" ,"POST"])
def movie_list(request):
    if request.method =="GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies , many = True)
        return Response(serializer.data)
    if request.method == "POST":
        data = request.data
        serializer= MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status= status.HTTP_201_CREATED)
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)

        
        
@api_view(["GET", "PUT","DELETE"])
def movie_detail(request , id):
    if request.method == "GET":
        movie = get_object_or_404(Movie , id = id) 
        serializer  = MovieSerializer(movie)
        return Response(serializer.data)
    
    if request.method =="PUT":
        movie = get_object_or_404(Movie , id = id)
        serializer = MovieSerializer(movie,data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status= status.HTTP_201_CREATED)
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
    if request.method =="DELETE":
        movie = get_object_or_404(Movie, id = id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)