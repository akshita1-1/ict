from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phoneno = models.BigIntegerField()
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="products")
    product = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)  # ✅ store line total

    def save(self, *args, **kwargs):
        # ✅ Auto-calculate total before saving
        discounted_price = self.price - (self.price * self.discount / 100)
        self.total = discounted_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product} ({self.customer.name})"
