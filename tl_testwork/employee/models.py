from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Employee(models.Model):
    """
    Работник
    """
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
    salary = models.IntegerField()
    department = TreeForeignKey(
        'Department',
        on_delete=models.PROTECT,
        related_name='employees',
        verbose_name='Работник'
    )
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return self.full_name


class Department(MPTTModel):
    """
    Подразделение
    """
    name = models.CharField(max_length=100)
    parent = TreeForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        db_index=True,
        related_name='children',
    )
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def get_absolute_url(self):
        return reverse('department-tree', args=[str(self.slug)])

    def __str__(self):
        return self.name
