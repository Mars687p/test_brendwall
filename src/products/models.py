from django.db import models


class Products(models.Model):
    name = models.CharField(verbose_name='Наименование',
                            max_length=128)
    description = models.TextField(verbose_name='Описание',
                                   null=True,
                                   blank=True)
    price = models.PositiveIntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self) -> str:
        return self.name
