from django.urls import path,include
from watchlist_app.api.views import (
    streamPlatformDetails,
    StreamPlatformAV ,
    watchListAV,
    WatchListDetailAV,
    ReviewCreate,
    ReviewDetail,
    ReviewList,
    #StreamPlatformView
)
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register("stream", StreamPlatformView, basename="stream-platform")


urlpatterns = [
    path("list/" , watchListAV.as_view() ,name = "movie-list"),
    path("list/<int:pk>" , WatchListDetailAV.as_view() ,name = "movie-detail"),
    # path("",include(router.urls)),
    path("stream/" , StreamPlatformAV.as_view() ,name = "stream-list"),
    path("stream/<int:pk>" , streamPlatformDetails.as_view() ,name = "stream-detail"),
    
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    
]
