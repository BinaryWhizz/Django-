from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class BinaryVarity(models.Model):
    BINARY_TYPES = [
        ('ML', 'MACHINE LEARNING'),
        ('PY', 'PYTHON'),
        ('DB', 'DBMS'),
        ('DJ', 'DJANGO'),
        ('DS', 'DATA SCIENCE'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='binarysss/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=BINARY_TYPES)
    description = models.TextField(default='')


    def __str__(self):
        return self.name



# 1)	One to many

class BinaryReview(models.Model):
    binary = models.ForeignKey(BinaryVarity, on_delete=models.CASCADE, related_name='reviews')   # CASCADE: When the parent record is deleted, all related child records are automatically deleted. It’s a referential integrity rule used with foreign keys.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField() 
    date_added = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return f'{self.user.username} review for {self.binary.name}'


# 2)	Many to many 

class Student(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    binary_varieties = models.ManyToManyField(BinaryVarity, related_name='students') 

    def __str__(self):
        return self.name


# 3)	One to one 

class Certificate(models.Model):
    binary = models.OneToOneField(BinaryVarity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField() 

    def __str__(self):
        return f'Certificate for {self.binary.name}' 