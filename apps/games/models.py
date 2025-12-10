from django.db import models
from django.utils.text import slugify
from django.db.models import Avg, Count


class Genre(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True)
    manufacturer = models.CharField(max_length=120, blank=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField(blank=True)
    genre = models.CharField(max_length=120, blank=True)
    developer = models.CharField(max_length=120, blank=True)
    publisher = models.CharField(max_length=120, blank=True)
    release_date = models.DateField(null=True, blank=True)
    genres = models.ManyToManyField(Genre, related_name='games', blank=True)
    platforms = models.ManyToManyField(Platform, related_name='games', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    @property
    def average_rating(self):
        return self.ratings.aggregate(value=Avg('value')).get('value') or 0

    @property
    def rating_count(self):
        return self.ratings.aggregate(total=Count('id')).get('total') or 0

    @property
    def review_count(self):
        return self.reviews.aggregate(total=Count('id')).get('total') or 0

    @property
    def favorites_count(self):
        return self.favorites.aggregate(total=Count('id')).get('total') or 0

    def get_absolute_url(self):
        return f"/games/{self.slug}/"


class Release(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='releases')
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='releases')
    region = models.CharField(max_length=80, blank=True)
    release_date = models.DateField()

    class Meta:
        ordering = ['release_date']
        unique_together = ('game', 'platform', 'region', 'release_date')

    def __str__(self) -> str:
        base = f"{self.game} on {self.platform}"
        return f"{base} - {self.release_date}" if self.release_date else base
