from django.contrib import admin
from .models import Category, Movies, review

# Register your models here.

admin.site.register(review)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class MoviesAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Movies,MoviesAdmin)