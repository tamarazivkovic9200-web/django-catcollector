from django.db import models



# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
      return self.name


# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)

    def __str__(self):
      return self.name

# Add new Feeding model below Cat model
class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(
    max_length=1, choices=MEALS, default=MEALS[0][0])
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    def __str__(self):
      return f"{self.get_meal_display()} on {self.date}"
    class Meta: ordering = ['-date']


