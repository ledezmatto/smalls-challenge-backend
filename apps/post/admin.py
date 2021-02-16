from django.contrib import admin

# Register your models here.
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
    )  
def _register(model, admin_class):
    admin.site.register(model, admin_class)
	
	
_register(Post, PostAdmin)