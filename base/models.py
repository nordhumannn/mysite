from django.core.validators import RegexValidator
from django.db import models
import uuid
import os
import datetime


class Category(models.Model):
    name = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)


class Dish(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('dishes/', new_filename)

    slug = models.SlugField(max_length=200, db_index=True)
    name = models.CharField(unique=True, max_length=50, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=500, blank=True)
    ingredients = models.CharField(max_length=200)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField()
    special = models.BooleanField(default=False)
    image = models.ImageField(upload_to=get_file_name)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.price}$'

    class Meta:
        ordering = ('position', 'price')
        index_together = (('id', 'slug'),)


class Event(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('events/', new_filename)

    name = models.CharField(max_length=50, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=200, blank=True)
    paragraph_1 = models.CharField(max_length=100, blank=True)
    paragraph_2 = models.CharField(max_length=100, blank=True)
    paragraph_3 = models.CharField(max_length=100, blank=True)
    is_visible = models.BooleanField(default=True)
    image = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.name}, {self.price}$'


class Gallery(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('gallery/', new_filename)

    image = models.ImageField(upload_to=get_file_name)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)


class Chefs(models.Model):
    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('chefs/', new_filename)

    image = models.ImageField(upload_to=get_file_name)
    name = models.CharField(max_length=30, db_index=True)
    job_title = models.CharField(max_length=30)
    position = models.SmallIntegerField(unique=True)
    insta_link = models.CharField(max_length=100, blank=True)
    twitter_link = models.CharField(max_length=100, blank=True)
    facebook_link = models.CharField(max_length=100, blank=True)
    linked_link = models.CharField(max_length=100, blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}, {self.job_title}'


class WhyUs(models.Model):

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class AboutUs(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('about/', new_filename)

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    paragraph_1 = models.CharField(max_length=200, blank=True)
    paragraph_2 = models.CharField(max_length=200, blank=True)
    paragraph_3 = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to=get_file_name)
    link = models.CharField(max_length=100)

    def __str__(self):
        return f'About #{self.pk}'


class Testimonials(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('testimonials/', new_filename)

    image = models.ImageField(upload_to=get_file_name)
    name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    stars = models.SmallIntegerField()
    review = models.TextField(max_length=200)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}, {self.job_title}'


class UserReservation(models.Model):

    mobile_re = RegexValidator(regex=r"^(\d{3}[- .]?){2}\d{4}$", message='Incorrect phone number (xxx xxx xxxx)')
    email_re = RegexValidator(regex=r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$",
                              message='Incorrect email')
    date_re = RegexValidator(
        regex=r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$",
        message='Incorrect date')
    time_re = RegexValidator(regex=r"^(?:[01]?\d|2[0-3])(?::[0-5]\d){1,2}$", message='Incorrect time')
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, validators=[email_re], blank=True)
    phone_number = models.CharField(max_length=15, validators=[mobile_re])
    date = models.CharField(max_length=10, validators=[date_re])
    time = models.CharField(max_length=5, validators=[time_re])
    people = models.PositiveSmallIntegerField()
    message = models.TextField(max_length=200, default='')
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date', '-is_processed',)

    def __str__(self):
        return f'{self.name}, {self.phone_number}, {self.message[:50]}'

