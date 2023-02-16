from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from django.db import models


# Members
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
    workday = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Members"


# product (hozircha -> ho'limlar)
class Product(models.Model):
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="content/nav-about-product-icon")
    img = models.ImageField(upload_to="content/nav-about-product-img", blank=True, null=True)
    content = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _("Bo'limlar")
        verbose_name = _("Bo'lim")


# Resources
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


# Announcement (E'lonlar)
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


# Services (Xizmatlar)
class Services(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="content/services-icons", help_text=_("icon"))
    email = models.EmailField(blank=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True)

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Xizmatlar")
        verbose_name = _("Xizmat")


class EmailMessages(models.Model):
    services = models.ForeignKey(to=Services, related_name="services", on_delete=models.CASCADE)

    name = models.CharField(verbose_name="FISH or Name organization", max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    message = models.TextField()
    file = models.FileField(null=True, blank=True, upload_to="file-message/")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.email}-{self.created_at}"

    class Meta:
        verbose_name_plural = _("Email xabarlar")
        verbose_name = _("Email xabari")


# InformationService (Axborot xizmatlari)
class InformationService(models.Model):
    class InformationServiceCat(models.TextChoices):
        NEWS = 'NS', _('NEWS')
        PHOTO_REPORT = 'PR', _("PHOTO REPORT")
        MEMORANDUM = 'MM', _("MEMORANDUM")
        OAV_ABOUT_US = 'oav', _("OAV ABOUT US")
        VIDEO_REPORT = 'VR', _("VIDEO REPORT")

    info_cat = models.CharField(max_length=3, choices=InformationServiceCat.choices)

    title = models.CharField(max_length=255)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    views_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _("Axborat xizmatlari")
        verbose_name = _("Axborat xizmati")


class ContentAdditionalFiles(models.Model):
    content = models.ForeignKey(to=InformationService, on_delete=models.CASCADE, related_name="content_files")
    file = models.FileField(upload_to="content/content-files",
                            validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'mp4'])])

    @property
    def is_video(self):
        if self.file:
            if str(self.file.url).split(".")[-1] == "mp4":
                return True
        return False

    def save(self, *args, **kwargs):
        if (self.content.info_cat == InformationService.InformationServiceCat.VIDEO_REPORT) or (
                self.content.info_cat == InformationService.InformationServiceCat.OAV_ABOUT_US):
            if str(self.file.url).split(".")[-1] == "mp4":
                super(ContentAdditionalFiles, self).save(*args, **kwargs)
        else:
            super(ContentAdditionalFiles, self).save(*args, **kwargs)

        # super(ContentAdditionalFiles, self).save(*args, **kwargs)


# Contact Uz
class ContactUs(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="full name or organization name")
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}-{self.email}-{self.created_at}"

    class Meta:
        verbose_name_plural = _("Contacts")
        verbose_name = _("Contact")


# Partners (hamkorlar)
class Partners(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="media/partners-icon")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Partners")
        verbose_name = _("Partner")


# Statistics (statistika hozircha ruchnoy)
class Statistics(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.value}"

    class Meta:
        verbose_name_plural = _("Statistics")
        verbose_name = _("Statistic")
