from django.db import models
from solo.models import SingletonModel

class ServiceCategory(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()

    class Meta:
        verbose_name_plural = "Категории услуг"

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Услуги"

    def __str__(self):
        return "%s - %s" % (self.name, self.price)


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = "Доктора"

    def __str__(self):
        return self.name


class ServiceImage(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    
    class Meta:
        verbose_name_plural = "Оказываемые услуги(фото)"

    def __str__(self):
        return self.name

class DocumentImage(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    
    class Meta:
        verbose_name_plural = "Документы, лицензии(фото)"

    def __str__(self):
        return self.name

class LegalInformation(models.Model):
    name = models.CharField(max_length=255)
    document = models.FileField()
    
    class Meta:
        verbose_name_plural = "Правовая информация"
    
    def __str__(self):
        return self.name
    
class Contact(SingletonModel):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    schedule = models.CharField(max_length=255)
    
    def __str__(self):
        return "Контакты"

    class Meta:
        verbose_name = "Контакты"  
