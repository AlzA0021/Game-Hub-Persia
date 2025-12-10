from django.db import models
from django.contrib.auth.models import User

from apps.games.models import Game


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='ratings')
    value = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'game')
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f"{self.value} for {self.game}"
