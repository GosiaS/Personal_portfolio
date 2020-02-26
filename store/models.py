from django.db import models
#from django.contrib.auth import get_user_model

class Category(models.Model):
    title = models.CharField(max_length=300)
    primaryCategory = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class  Product(models.Model):
    #image = models.ImageField(upload_to='store/static/img', blank=True)
    image = models.FilePathField(path="store/static/img")
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_text = models.TextField()
    detail_text = models.TextField()
    price = models.FloatField()
    
    def __str__(self):
        return self.name

'''
# Get the user model
User = get_user_model()


# Cart Model
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.quantity} of {self.item.name}'

class Order(models.Model):
    orderitems  = models.ManyToManyField(Cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

'''