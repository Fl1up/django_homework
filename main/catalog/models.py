from django.db import models
from django.db.models import Model

NULLABLE = {
    "null": True,
    "blank": True
}


class Category(Model):
    title = models.CharField(max_length=20, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", **NULLABLE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(Model):

    title = models.CharField(max_length=100, verbose_name="Название", unique=True)  # unique - уникальность
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="catalog/media/", **NULLABLE, verbose_name="Изображние")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    price = models.FloatField(verbose_name="Цена за товар", **NULLABLE)
    creations_date = models.DateField(verbose_name="Дата создания", **NULLABLE)
    last_change_date = models.DateField(**NULLABLE, verbose_name="Дата последнего изменения")
    is_published = models.BooleanField(default=True)
    views_count = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return f"{self.title} {self.category} {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"



