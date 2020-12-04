from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

def upload_gallery_image(instance, filename):
    return f"images/{instance.pet.name}/gallery/{filename}"

class Image(models.Model):
    image = models.ImageField(upload_to=upload_gallery_image)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="images")
