from django.contrib import admin
from .models import Sp_user

# Register your models here.
class SpuserAdmin(admin.ModelAdmin):
    # dupple
    list_display = ('username','password')

admin.site.register(Sp_user,SpuserAdmin)