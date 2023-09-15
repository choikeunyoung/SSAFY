from django.contrib import admin
from practice4.models import Practice4_Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ["pk","title","genre","director"]
    fieldsets = [
        (None, {"fields":("title","genre","director")})
    ]
admin.site.register(Practice4_Movie, MovieAdmin)
