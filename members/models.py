from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models import CharField

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


def image_upload(inistance, filename):
    imagename, extention = filename.split(".")
    return "members/%s.%s" % (inistance.id, extention)


class Members(models.Model):
    member_no = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    member_name: CharField = models.CharField(blank=True, null=True, max_length=200)
    id_no = models.CharField(max_length=25)
    created_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    member_type = models.CharField(max_length=25, choices=MEMBER_TYPES)
    gender = models.CharField(max_length=25, choices=GENDER)
    member_image = models.ImageField(blank=True, null=True, upload_to=image_upload)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.member_name = self.first_name + ' ' + self.middle_name + ' ' + self.last_name
        self.slug = '9875' + self.member_no + '1245'
        super(Members, self).save(*args, **kwargs)

    def __str__(self):
        return self.member_name
