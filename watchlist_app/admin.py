from django.contrib import admin
from .models import WatchList,StreamPlatform,Review
# Register your models here.


class watchListAdminView(admin.ModelAdmin):
    list_display = ["id", "title", "storyline"]

admin.site.register(WatchList,watchListAdminView)
admin.site.register(StreamPlatform)




class ReviewAdminView(admin.ModelAdmin):
    list_display = ["id", "rating", "review_user"]

admin.site.register(Review, ReviewAdminView)