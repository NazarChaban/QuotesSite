from django.contrib.auth.models import User
from django.db import models
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        default='default_avatar.png',
        upload_to='profile_images'
    )

    def __str__(self):
        return self.user.username
    
    #resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        conditions = (img.height > 250, img.width > 250)
        if any(conditions):
            new_size = (250, 250)
            img.thumbnail(new_size)
            img.save(self.avatar.path)
