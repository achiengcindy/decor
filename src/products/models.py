from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# from .checkout.models import OrderItem,Order

User = get_user_model()


class ActiveCategoryManager(models.Manager):
    def get_query_set(self):
        return super(ActiveCategoryManager, self).get_query_set().filter(is_active=True)

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for product page URL, created from name.')
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    meta_description = models.CharField("Meta Description", max_length=255, help_text='Content for description meta tag')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    active = ActiveCategoryManager()
    
    class Meta:
        db_table = 'categories'
        ordering = ('-created',)
        verbose_name = 'category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('products:list_category',args=[ self.slug])

class ActiveProductManager(models.Manager):
    def get_query_set(self):
        return super(ActiveProductManager, self).get_query_set().filter(is_active=True)
class FeaturedProductManager(models.Manager):
    def all(self):
        return super(FeaturedProductManager, self).all().filter(is_active=True).filter(is_featured=True)

class Product(models.Model):
    """ model class containing information about a product; instances of this class are what the user
    adds to their shopping cart and can subsequently purchase
    
    """
    name = models.CharField(max_length=190, db_index=True)
    slug = models.SlugField(max_length=190, db_index=True)
    brand = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    old_price = models.DecimalField(max_digits=9,decimal_places=2, blank=True,default=0.00)
    # image fields
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    image_caption = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    meta_description = models.CharField(max_length=255, help_text='Content for description meta tag')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)

    objects = models.Manager()
    active = ActiveProductManager()
    featured = FeaturedProductManager()

    class Meta:
        db_table = 'products'
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('products:product_detail',args=[self.slug])
        return reverse('products:product_detail',args=[self.id,self.slug])

     
    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None

    
    # def cross_sells(self):
    #     orders = Order.objects.filter(orderitem__product=self)
    #     order_items = OrderItem.objects.filter(order__in=orders).exclude(product=self)
    #     products = Product.active.filter(orderitem__in=order_items).distinct()
    #     return products

    # # users who purchased this product also bought....
    # def cross_sells_user(self):
    #     """ gets other Product instances that have been ordered by other registered customers who also ordered the current
    #     instance. Uses all past orders of each registered customer and not just the order in which the current 
    #     instance was purchased
    #     """
    #     from checkout.models import Order, OrderItem
    #     users = User.objects.filter(order__orderitem__product=self)
    #     items = OrderItem.objects.filter(order__user__in=users).exclude(product=self)
    #     products = Product.active.filter(orderitem__in=items).distinct()
    #     return products
   

    # def cross_sells_hybrid(self):
    #         """ gets other Product instances that have been both been combined with the current instance in orders placed by 
    #         unregistered customers, and all products that have ever been ordered by registered customers
    #         """
    #         from checkout.models import Order, OrderItem
    #         from django.db.models import Q
    #         orders = Order.objects.filter(orderitem__product=self)
    #         users = User.objects.filter(order__orderitem__product=self)
    #         items = OrderItem.objects.filter( Q(order__in=orders) | 
    #                     Q(order__user__in=users) 
    #                     ).exclude(product=self)
    #         products = Product.active.filter(orderitem__in=items).distinct()
    #         return products
