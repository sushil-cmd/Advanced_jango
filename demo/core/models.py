from django.conf import settings
from django.db import models
from django.shortcuts import reverse

CATEGORY_CHOICES=(
    ('S','Shirt'),
    ('SW','Sport wear'),
    ('OW','Outwear'),
)
LABLE_CHOICES=(
    ('P','primary'),
    ('S','secondary'),
    ('D','danger'),
)

class Item(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True,null=True)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    label = models.CharField(choices=LABLE_CHOICES, max_length=1)
    slug = models.SlugField()
    description=models.TextField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('core:product',kwargs={
            'slug':self.slug
        })


class OrderItem(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)

    def __str__(self):
        return self.item


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username