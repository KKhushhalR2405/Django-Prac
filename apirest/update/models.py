from pyexpat import model
from django.db import models
from django.conf import settings
# Create your models here.

def upload_update_image(instance,filename):
    return "update/{user}/filename".format(instance.user,filename)

class UpdateModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    content = models.TextField(blank = True, null= True)
    image = models.ImageField(upload_to = upload_update_image,
                            blank = True, null= True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.content or ""