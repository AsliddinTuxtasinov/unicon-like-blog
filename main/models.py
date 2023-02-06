from ckeditor.fields import RichTextField
from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class SubCategories(models.Model):
    parent = models.ForeignKey(to=Categories, on_delete=models.CASCADE, related_name="parent_category")
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    is_services = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Custom logic to be executed before saving the instance to the database
        if self.email:
            self.is_services = True
        super().save(*args, **kwargs)
        # Custom logic to be executed after saving the instance to the database
        # ...

    class Meta:
        verbose_name_plural = "Sub categories"


class Content(models.Model):
    title = models.CharField(max_length=255)
    # content = models.TextField()
    content = RichTextField()
    created_at = models.DateField(auto_now_add=True)

    sub_category = models.ForeignKey(to=SubCategories, on_delete=models.CASCADE, related_name="content_sub_category")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Contents"


class ContentImages(models.Model):
    content = models.ForeignKey(to=Content, on_delete=models.CASCADE, related_name="content_images")
    image = models.ImageField(upload_to="content/content-images")


class EmailMessages(models.Model):
    services = models.ForeignKey(to=SubCategories, related_name="services", on_delete=models.CASCADE)

    name_organization = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    message = models.TextField()
    file = models.FileField(null=True, blank=True, upload_to="file-message/")
    is_agree = models.BooleanField()

    created_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}-{self.email}-{self.created_add}"

    class Meta:
        verbose_name_plural = "Email messages"
