from django.db import models

class SpotifyFavorites(models.Model):
    song_name = models.CharField(max_length=200)
    artist_name = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    song_url = models.URLField(unique=True)
    duration_ms = models.IntegerField()
    added_at = models.DateTimeField()

    class Meta:
        ordering = ['-added_at']
        verbose_name = 'Canción Favorita'
        verbose_name_plural = 'Canciones Favoritas'

    def __str__(self):
        return f"{self.song_name} - {self.artist_name}"

class SpotifyTopSongs(models.Model):
    song_name = models.CharField(max_length=200)
    artist_name = models.CharField(max_length=200)
    song_url = models.URLField()

    class Meta:
        verbose_name = 'Canción Top'
        verbose_name_plural = 'Canciones Top'

    def __str__(self):
        return f"{self.song_name} - {self.artist_name}"

class DeletedSongs(models.Model):
    song_name = models.CharField(max_length=200)
    artist_name = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    song_url = models.URLField()
    duration_ms = models.IntegerField()
    added_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        ordering = ['-deleted_at']
        verbose_name = 'Canción Eliminada'
        verbose_name_plural = 'Canciones Eliminadas'

    def __str__(self):
        return f"{self.song_name} - {self.artist_name}"