from django.contrib import admin
from api.models import Platform, Publisher, Genre, Type, Screenshot, Game
# Register your models here.
admin.site.register(Platform)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Type)
admin.site.register(Screenshot)
admin.site.register(Game)