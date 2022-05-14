from django.db import models


class Nationality(models.Model):
    country = models.CharField(max_length=300, unique=True)
    country_flag = models.ImageField(null=True, blank=True, upload_to='media/country_flag')

    class Meta:
        ordering = ('country', )

    def __str__(self):
        return self.country


class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    country = models.ForeignKey(Nationality, related_name='players', on_delete=models.CASCADE)
    birth_day = models.DateField()

    class Meta:
        ordering = ('-birth_day', )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Competition(models.Model):
    name = models.CharField(max_length=200, unique=True)
    players = models.ManyToManyField(Player, related_name='competitions')
    award = models.DecimalField(decimal_places=0, max_digits=9)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name




