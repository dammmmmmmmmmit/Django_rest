from django.contrib import admin
from .models import User,Contact,Spam

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','phone')
    search_fields= ('username','email','phone')
    list_filter=('is_staff','is_active')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display =('owner','name','phone')
    search_fields =('owner__username', 'name','phone')
    list_filter=('owner',)

@admin.register(Spam)
class SpamAdmin(admin.ModelAdmin):
    list_display=('reporter','phone')
    search_fields=('reporter__username','phone')
    list_filter=('reporter',)
    