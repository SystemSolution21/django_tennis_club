from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    join_date = models.DateField(null=True)
    slug = models.SlugField(null=False, default="")

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"
