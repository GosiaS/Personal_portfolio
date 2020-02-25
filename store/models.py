from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=300)
    primaryCategory = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class  Product(models.Model):
    image = models.ImageField(upload_to='store/static/img', blank=True)
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_text = models.TextField()
    detail_text = models.TextField()
    price = models.FloatField()
    
    def __str__(self):
        return self.name
