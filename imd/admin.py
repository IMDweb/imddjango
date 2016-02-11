from django.contrib import admin
from imd.models import Service, Category, Gallery

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
	exclude = ['posted']
	prepopulated_fields = { 'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ('name',)}

admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Gallery)