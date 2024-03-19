from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
    
    # title = models.CharField(
    #     verbose_name = "Название категории",
    #     max_length = 255,
    # )
    # is_active = models.BooleanField(default = False)
    # created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add = True)
    # updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now = True)

class Post(models.Model):
    status_choises = (
        ('ACTIVE','Active'),
        ('DRAFT','Draft')   
    )
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.author} on '{self.post}'"