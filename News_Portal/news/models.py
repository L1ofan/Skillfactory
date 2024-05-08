from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        posts_rating = 0
        comments_rating = 0
        posts_comments_rating = 0
        post = Post.objects.filter(author=self)
        for p in post:
            posts_rating += p.rating
        comments = Comment.objects.filter(user=self.user)
        for c in comments:
            comments_rating += c.rating
        posts_comments = Comment.objects.filter(post__author=self)
        for pc in posts_comments:
            posts_comments_rating += pc.rating

    def __str__(self):
        return self.user.username

        self.rating = posts_rating * 3 + comments_rating + posts_comments_rating
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=64,unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    article = 'AR'
    news = 'NE'

    POSITTIONS = [
        (article, 'Статья'),
        (news, 'Новости')
    ]
    post_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    post_type = models.CharField(max_length=2,default=news)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        small_text = self.text[0:124] + '...'
        return small_text

    def __str__(self):
        return f'{self.text[:20]}'

    def get_absolute_url(self):
        return reverse('Post', args=[str(self.id)])


class PostCategory(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
