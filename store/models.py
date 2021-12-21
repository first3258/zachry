from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255, unique=True)
    slug=models.SlugField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('product_by_category', args=[self.slug])

class Product(models.Model):
    name=models.CharField(max_length=255, unique=True)
    author=models.CharField(max_length=255,  blank=True)
    slug=models.SlugField(max_length=255, unique=True)
    desciption=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="", blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('productDetail', args=[self.category.slug, self.slug])


class Cart(models.Model) :
    card_id = models.CharField(max_length = 255, blank = True)
    date_added = models.DateTimeField(auto_now_add = True)
    user = models.IntegerField(blank = True, default = 0)
    
    def __str__(self):
        return self.card_id

    class Meta:
        ordering = ('date_added', )

class CartItem(models.Model) :
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    

    def sub_total(self):
        return self.product.price * self.quantity 

    def __str__(self):
        return self.product.name
    
class Order(models.Model):
    name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    postcode = models.CharField(max_length=255, blank=True)
    total = models.DecimalField(max_digits = 10, decimal_places = 2)
    email = models.EmailField(max_length = 255, blank=True)
    token = models.CharField(max_length=255, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    A = 'กำลังเตรียมคำสั่งซื้อ'
    B ='กำลังจัดส่ง'
    C = 'จัดส่งสำเร็จ'
    Status_List = [
    (A, 'กำลังเตรียมคำสั่งซื้อ'),
    (B, 'กำลังจัดส่ง'),
    (C, 'จัดส่งสำเร็จ'),
    ]
    status=models.CharField(max_length=255, blank=True, choices=Status_List, default=A)

    class Meta:
        ordering = ('-id',)


    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.CharField(max_length = 250)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    order = models.ForeignKey(Order, on_delete= models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)


    def sub_total(self):
        return self.quantity*self.price

    class Meta:
        ordering = ('-order',)


    def __str__(self):
        return self.product
    
