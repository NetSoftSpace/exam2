from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Company(BaseModel):
    name = models.CharField(verbose_name=_("Name"), max_length=222)
    desc = models.TextField(verbose_name=_("Description"))
    image = models.ImageField(verbose_name=_("Image"), upload_to="company/images/")

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(verbose_name=_("Name"), max_length=222)
    image = models.ImageField(verbose_name=_("Image"), upload_to="company/images/")
    company = models.ForeignKey(Company, verbose_name=_("Company"))
    discount = models.CharField(
        verbose_name=_("Discount"),
        max_length=20,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class User(AbstractUser, BaseModel):
    name = models.CharField(verbose_name=_("Name"), max_length=222)
    member = models.ManyToManyField(Company, verbose_name=_("Member"))

    def __str__(self):
        return self.name


class Review(BaseModel):
    company = models.ForeignKey(Company, verbose_name=_("Company"))
    user = models.ForeignKey(User, verbose_name=_("User"))
    comment = models.TextField(verbose_name=_("Comment"))
    rating = models.IntegerField(verbose_name=_("Rating"), max_length=1, null=True, blank=True)

    def __str__(self):
        return f" {self.rating} {self.comment}"
