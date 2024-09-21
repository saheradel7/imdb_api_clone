from watchlist_app.models import WatchList,StreamPlatform, Review
from rest_framework.decorators import api_view
from watchlist_app.api.serializers import WatchListSerializer,StreamPlatformSerializer,ReviewsSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import generics
from rest_framework.exceptions import ValidationError
class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewsSerializer
    queryset =Review.objects.all()
    def perform_create(self, serializer):
        pk = self.kwargs.get("pk")
        watch_list = WatchList.objects.get(id=pk)
        review_user= self.request.user
        review_watch_list = Review.objects.filter(watch_list = watch_list , review_user = review_user)
        if review_watch_list.exists():
            raise ValidationError("you have reviewed this movie before")
        serializer.save(WatchList = watch_list)
        
class ReviewList(generics.ListAPIView):
    
    serializer_class = ReviewsSerializer
    
    def get_queryset(self):
        pk =self.kwargs.get("pk")
        return Review.objects.filter(watch_list = pk)        
        
        
        
class ReviewDetail(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer
    
    def post(self, request, *args, **kwargs):
        review_id = kwargs.get("pk")
        review = Review.objects.get(id =review_id)
        if review.review_user == request.user:
            review.rating = request.data
        return super().put(request, *args, **kwargs)



# class StreamPlatformView(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         platform = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(platform)
#         return Response(serializer.data)


class StreamPlatformAV(APIView):
    def get(self, request):
        platforms = StreamPlatform.objects.all()
        ser = StreamPlatformSerializer(platforms,many =True,context={'request': request})
        return Response(ser.data , status= status.HTTP_200_OK)
    
    def post(self,request):
        ser = StreamPlatformSerializer(data = request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status= status.HTTP_201_CREATED)
        return Response(ser.errors , status= status.HTTP_400_BAD_REQUEST)


class streamPlatformDetails(APIView):
    
    def get(self, request , pk):
        platform = get_object_or_404(StreamPlatform, id = pk)
        ser = StreamPlatformSerializer(platform)
        return Response(ser.data, status=status.HTTP_200_OK)
    
    def put(self , request,pk):
        platform = get_object_or_404(StreamPlatform , id = pk)
        ser = StreamPlatformSerializer(platform , data = request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status= status.HTTP_201_CREATED)
        return Response(ser.errors , status= status.HTTP_400_BAD_REQUEST)
    def delete(self,request , pk):
        platform = get_object_or_404(StreamPlatform , id = pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

class watchListAV(APIView):    
    def get(self,request):
        movies = WatchList.objects.all()
        ser = WatchListSerializer(movies , many =True)
        return Response(ser.data , status= status.HTTP_200_OK)
    
    def post(self,request):
        ser = WatchListSerializer(data = request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data , status=status.HTTP_200_OK)
        return Response(ser.errors , status= status.HTTP_400_BAD_REQUEST)
        
class WatchListDetailAV(APIView):
    def get(self,request,pk):
        movie = get_object_or_404(WatchList, id =pk)
        ser = WatchListSerializer(movie)
        return Response(ser.data , status=status.HTTP_200_OK)
    
    
    def put(self,request,pk):
        movie = get_object_or_404(WatchList,id=pk)
        ser = WatchListSerializer(movie,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data , status=status.HTTP_200_OK)
        return Response(ser.errors , status= status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        movie = get_object_or_404(WatchList,id=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    


# @api_view(["GET" ,"POST"])
# def movie_list(request):
#     if request.method =="GET":
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies , many = True)
#         return Response(serializer.data)
#     if request.method == "POST":
#         data = request.data
#         serializer= MovieSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data ,status= status.HTTP_201_CREATED)
#         return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)

        
        
# @api_view(["GET", "PUT","DELETE"])
# def movie_detail(request , id):
#     if request.method == "GET":
#         movie = get_object_or_404(Movie , id = id) 
#         serializer  = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method =="PUT":
#         movie = get_object_or_404(Movie , id = id)
#         serializer = MovieSerializer(movie,data =request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data ,status= status.HTTP_201_CREATED)
#         return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
#     if request.method =="DELETE":
#         movie = get_object_or_404(Movie, id = id)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)