from django.contrib import admin
from .models import Profile,Articles,Category,Tags,Rooms

# Register your models here.
class ArticlesAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Profile)
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Rooms)