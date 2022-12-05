from django.db import models

# Create your models here.
SEX = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]
STATUS = [
    ('Wanted', 'Wanted'),
    ('Released', 'Released'),
    ('Free', 'Free'),
]


def img_path(instance, filename):
    return f"{instance.full_name}/{filename}"


class Criminal(models.Model):
    full_name = models.CharField(max_length=255)
    sex = models.CharField(max_length=20, choices=SEX)
    # dob = models.DateField()
    # national_id = models.IntegerField()
    address = models.CharField(max_length=255)
    criminal_status = models.CharField(max_length=20, choices=STATUS)
    image_1 = models.ImageField(upload_to=img_path, blank=True, null=True)
    image_2 = models.ImageField(upload_to=img_path, blank=True, null=True)
    image_3 = models.ImageField(upload_to=img_path, blank=True, null=True)
    image_4 = models.ImageField(upload_to=img_path, blank=True, null=True)
    image_5 = models.ImageField(upload_to=img_path, blank=True, null=True)

    def __str__(self):
        return self.full_name
