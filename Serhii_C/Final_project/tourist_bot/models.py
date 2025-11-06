from django.db import models

# Create your models here.

EXCURSION_TYPES = (
    ('foot', 'Пішохідна'),
    ('bus_1', 'Автобусна (1 день)'),
    ('bus_2', 'Автобусна (2 дні)'),
)

class Excursion(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=20000, blank=True, null=True,verbose_name="Детальний опис")
    type = models.CharField(max_length=200, choices=EXCURSION_TYPES,default='foot', blank=True, null=True,verbose_name="Тип екскурсії")
    keyword = models.CharField(max_length=200)
    is_lunch_included = models.BooleanField(default=False, verbose_name="Обід включено")
    price = models.DecimalField(decimal_places=2,max_digits= 100,verbose_name="Ціна")
    conditions = models.TextField(max_length=20000, blank=True, null=True,verbose_name="Умови і оплата")
    vidguki = models.TextField(max_length=20000, blank=True, null=True,verbose_name="Відгуки")

    def __str__(self):
        return self.title





