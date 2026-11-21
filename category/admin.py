from django.contrib import admin
from category.models import CategoryModel

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("user", "name",)
