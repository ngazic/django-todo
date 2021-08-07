from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class TodoList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(default=0, max_digits=4, decimal_places=2)
    done = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, default='General',on_delete=CASCADE)
    
    @property
    def total_cost(self):
        return self.quantity * self.price
    
    def __str__(self) -> str:
        return f'{self.quantity} - {self.title}'
    
    class Meta:
        ordering = ['-price']
