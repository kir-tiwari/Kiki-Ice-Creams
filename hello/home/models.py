
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    comment = models.TextField()
    date = models.DateField()

    # If you want to display name in the model object
    def __str__(self):
        return self.name


# makemigartion - Create changes and store in a file
# migarte - Apply the pending changes created by makemigrations
