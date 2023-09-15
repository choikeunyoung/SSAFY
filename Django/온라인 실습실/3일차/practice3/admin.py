from django.contrib import admin
from practice3.models import Practice3_Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["pk","title","content","created_at","updated_at"]

admin.site.register(Practice3_Article, ArticleAdmin)
