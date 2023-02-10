from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.db import models


class Members(models.Model):
    class MembersCat(models.TextChoices):
        LEADERSHIP = 'RT', _('RAXBARIYAT')
        SCIENTIFIC_COUNCIL = 'IK', _('ILMIY KENGASH')
        OUR_TEAM = 'BJ', _('BIZNING JAMOA')

    member_type = models.CharField(max_length=2, choices=MembersCat.choices)
    image = models.ImageField(upload_to="content/member-image")
    full_name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    phone = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Members"


class Product(models.Model):
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="content/nav-about-product-icon")
    img = models.ImageField(upload_to="content/nav-about-product-img", blank=True, null=True)
    content = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _("Maxsulotlar")
        verbose_name = _("Maxsulot")


# Resource -> About Us
class Resource(models.Model):
    title = models.CharField(max_length=255)
    short_desc = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="content/nav-about-resource-icon")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _("Resurslar")
        verbose_name = _("Resurs")


class ResourceContent(models.Model):
    resource = models.ForeignKey(to=Resource, on_delete=models.CASCADE, related_name="resource_content")

    name = models.CharField(max_length=255)
    short_desc = models.CharField(max_length=255)
    file = models.FileField(upload_to="content/resource-content-file")
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = _("Resurs contentlari")
        verbose_name = _("Resurs conteni")


class Announcement(models.Model):
    class AnnouncementCat(models.TextChoices):
        COMPETITIONS = 'CS', _('KONKURSLAR')
        SELECTION_OF_PROPOSALS = 'IK', _('TAKLIFLAR_TANLOVI')

    class AnnouncementStatus(models.TextChoices):
        CONTINUE = 'CS', _("OZ_KUCHIDA")
        FINISHED = 'IK', _('MUDDATI_TUGAGAN')

    announcement_status = models.CharField(max_length=2, choices=AnnouncementCat.choices)
    status_type = models.CharField(max_length=2, choices=AnnouncementStatus.choices)

    title = models.CharField(max_length=255)
    content = RichTextField()
    started_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = _("E'lonlar")
        verbose_name = _("E'lon")


class Services(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField()

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Xizmatlar")
        verbose_name = _("Xizmat")


class InformationService(models.Model):
    class InformationServiceCat(models.TextChoices):
        NEWS = 'NS', _('YANGILIKLAR')
        PHOTO_REPORT = 'PR', _("FOTO REPORTAJ")
        VIDEO_REPORT = 'VR', _("VIDEO REPORTAJ")
        MEMORANDUM = 'MM', _("MEMORANDUM")

    info_cat = models.CharField(max_length=2, choices=InformationServiceCat.choices)

    title = models.CharField(max_length=255)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def views_count(self):
        return self.content_views_count.count()

    class Meta:
        verbose_name_plural = _("Axborat xizmatlari")
        verbose_name = _("Axborat xizmati")


class InformationServiceContentViewsModel(models.Model):
    content = models.ManyToManyField(to=InformationService, related_name="content_views_count")
    mac_address = models.CharField(max_length=255)


class ContentImages(models.Model):
    content = models.ForeignKey(to=InformationService, on_delete=models.CASCADE, related_name="content_images")
    image = models.ImageField(upload_to="content/content-images")


class EmailMessages(models.Model):
    services = models.ForeignKey(to=Services, related_name="services", on_delete=models.CASCADE)

    name_organization = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    message = models.TextField()
    file = models.FileField(null=True, blank=True, upload_to="file-message/")
    # is_agree = models.BooleanField()

    created_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}-{self.email}-{self.created_add}"

    class Meta:
        verbose_name_plural = _("Email xabarlar")
        verbose_name = _("Email xabari")


class ContactUs(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="full name or organization name")
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    message = models.TextField()

    created_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}-{self.email}-{self.created_add}"

    class Meta:
        verbose_name_plural = _("Contacts")
        verbose_name = _("Contact")


class Partners(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="media/partners-icon")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Partners")
        verbose_name = _("Partner")
