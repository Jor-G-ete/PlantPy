from django.db import models
from django.utils import timezone


# Creates a Plant
class Plant(models.Model):
    # Id
    id = models.AutoField(primary_key=True)
    # Characteristics
    name = models.TextField(max_length=100)
    born_in = models.DateTimeField(default=timezone.now)
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=3)
    heigth = models.FloatField()
    width = models.FloatField()
    level = models.IntegerField(default=1)

    # Needs
    water = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
    sunlight = models.FloatField(default=0)
    nutrients = models.FloatField(default=0)

    # Control of needs
    last_time_watered = models.DateField(default=born_in)
    last_time_fertilised = models.DateField(default=born_in)

    def water_plant(self):
        """
        Pour water into the plant automatically

        :return:
        :rtype:
        """

        pass

    def __str__(self):
        return self.name + " is at level: " + str(self.level)

