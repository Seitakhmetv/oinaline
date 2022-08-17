from tkinter import CASCADE
from django.db import models

class Platform(models.Model):
    title = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'Platform'

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title
        }
    def __str__(self):
        return self.title

class Publisher(models.Model):
    title = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'Publisher'

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title
        }
    def __str__(self):
        return self.title

class Genre(models.Model):
    title = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'Genre'

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title
        }
    def __str__(self):
        return self.title

class Type(models.Model):
    title = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'Type'

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title
        }
    def __str__(self):
        return self.title

class Screenshot(models.Model):
    name = models.CharField(max_length=200, default="NO GAME")
    url = models.CharField(max_length=2000)

    class Meta:
        verbose_name = 'Screenshot'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url,
        }
    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=300)
    platforms = models.ManyToManyField(Platform)
    screenshots = models.ManyToManyField(Screenshot)
    trailer = models.CharField(max_length=300)
    genres = models.ManyToManyField(Genre)
    types = models.ForeignKey(Type, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(Publisher)
    description = models.TextField()
    metacritic = models.IntegerField()

    class Meta:
        verbose_name = "Game"
    
    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'platforms': self.platforms,
            'screenshots': self.screenshots,
            'Publishers': self.publishers,
            'trailer': self.trailer,
            'genres': self.genres,
            'types': self.types,
            'description': self.description,
            'metacritic': self.metacritic
        }
    def __str__(self):
        return self.title
    

# 5 models{
#     game mode:
#         title,
#         backround_img,
#         [platform] = many to many,
#         [publisher] = many to many,
#         [screenshot] = many to many,
#         trailer = one to many,
#         [genres] = many to many,
#         type = one to many,
#         description,
#         metacritic
#     platform:
#         title,
#     publisher:
#         title,
#     genre:
#         title,
#     type:
#         title,
#     screenshot:
#         url,
# }