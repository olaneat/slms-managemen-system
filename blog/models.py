from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    slug = models.SlugField(max_length=150, null=True, blank=True)
    body = models.TextField()
    author = models.CharField(max_length=120, null=True, blank=True )
    img = models.FileField(upload_to='img/blog', null = True, blank=True)
    created = models.DateField()

    class Meta:
        ordering = ('created',)
        verbose_name = ('Post')
        verbose_name_plural = ('Posts')


    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.slug, self.created.year, self.created.month, self.created.day])
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    username = models.CharField(max_length= 150, blank=True, null=True)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    active = models.BooleanField(default=False)
    created = models.DateField(auto_now=True)


    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ('-created',)
    

