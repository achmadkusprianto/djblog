from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    judul = models.CharField(max_length=100)
    konten = models.TextField()
    tanggal_post = models.DateTimeField(default=timezone.now)
    pengarang = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.judul + '   <<dipost oleh>>   '+ str(self.pengarang)


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})