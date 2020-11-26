from django.db import models

# Create your models here.
MEMBER_TYPES = (
    ('Normal', 'Normal'),
    ('Active', 'Active'),
    ('Honer', 'Honer'),
)
GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

def image_upload(inistance,filename):
    imagename,extention = filename.split(".")
    return "members/%s.%s"%(inistance.id,extention)

class Members(models.Model):
    member_no = models.CharField(max_length=25)
    member_name = models.CharField(max_length=200)
    id_no = models.CharField(max_length=25)
    created_date = models.DateTimeField(auto_now=True)
    date_of_birth = models.DateField()
    member_type = models.CharField(max_length=25, choices=MEMBER_TYPES)
    gender = models.CharField(max_length=25, choices=GENDER)
    member_image = models.ImageField(upload_to=image_upload)

    def __str__(self):
        return self.member_name