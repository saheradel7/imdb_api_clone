# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse
# from django.shortcuts import get_list_or_404
# # Create your views here.


# def movie_list(request):
#     movies = Movie.objects.all()
#     print(movies.values())
#     data = {"data": list(movies.values())}
#     return JsonResponse(data , safe=False)


# def movie_detail(request,id):
#     movie = get_list_or_404(Movie , id = id)
#     print(movie)
#     data = {
#         "name" : movie.name,
#         "descriptions" :movie.description,
#         "active" : movie.active
#         }
#     return JsonResponse(data)