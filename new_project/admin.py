from django.contrib import admin
from .models import Category,New, Contacts

# admin.site.register(Category)
# admin.site.register(New)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ["title","slug","created_at","status"]
    list_filter = ["title","created_at","status"]
    prepopulated_fields = {"slug":("title",)}
    search_fields = ["title","slug"]



admin.site.register(Contacts)




