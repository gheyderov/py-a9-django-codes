from django.db import models

# Create your models here. 

class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BlogCategory(AbstractModel):
    title = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Blog Categories'


class Blog(AbstractModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey('BlogCategory', on_delete=models.CASCADE, related_name='blogs')
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return f'{self.title} - {self.category}'
