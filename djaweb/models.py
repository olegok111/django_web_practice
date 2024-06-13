# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _


class Client(models.Model):
    full_name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.full_name


class Film(models.Model):
	title = models.CharField(max_length=1000)
	genre = models.CharField(max_length=1000)
	company = models.CharField(max_length=1000)
	director = models.CharField(max_length=1000)
	release_year = models.IntegerField()
	purchase_price = models.IntegerField()
	rent_price = models.IntegerField()
	
	def __str__(self):
		return self.title


class Rental(models.Model):
	class RentalMethod(models.TextChoices):
		RENT = "R", _("Аренда")
		PURCHASE = "P", _("Покупка")

	film = models.ForeignKey(Film, on_delete=models.CASCADE)
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	rent_or_purchase = models.CharField(
		max_length=1,
		choices=RentalMethod.choices,
	)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	price = models.IntegerField()
	
	def __str__(self):
		return f"{self.rent_or_purchase};{self.film};{self.client}"

