from django.db import models
from accounts.models import User


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField("Rasm", upload_to='posts/')
    description = models.TextField("Tasnifi")
    is_archive = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='user_likes', null=True, blank=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Postlar"

    def __str__(self):
        return self.description[:50]


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments")
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField("Kommentariyalar")

    class Meta:
        verbose_name = "Kommentariya"
        verbose_name_plural = "Kommentariyalar"
        ordering = ['-created']

    def __str__(self):
        return f"{self.content}"[:100]


