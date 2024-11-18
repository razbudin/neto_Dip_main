from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# Класс публикации поста
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    image = models.ImageField(upload_to='photos')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} -- {self.text}'


# Класс предоставления лайка к посту
class Like(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='likes')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author.username} понравился {self.post}'


# Класс предоставления коментария к посту
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} - {self.text}'
