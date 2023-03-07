from django.db import models
from common.models import CommonModel

# from times.models import TimeModel


class Idol(models.Model):
    """Idol Model Definition"""

    class GroupChoices(models.TextChoices):
        GirlGroup = ("GirlGroup", "GirlGroup")
        BoyGroup = ("BoyGroup", "BoyGroup")

    class SoloChoices(models.TextChoices):
        GirlSolo = ("GirlSolo", "GirlSolo")
        BoySolo = ("BoySolo", "BoySolo")

    class GenderChoices(models.TextChoices):
        Woman = ("Woman", "Woman")
        Man = ("Man", "Man")

    idol_group = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        choices=GroupChoices.choices,
    )
    idol_solo = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        choices=SoloChoices.choices,
    )

    idol_name = models.CharField(max_length=7)
    idol_profile = models.URLField(max_length=10000, blank=True, null=True)

    idol_anniv = models.DateField()
    idol_birthday = models.DateField()

    idol_gender = models.CharField(
        max_length=5,
        choices=GenderChoices.choices,
    )

    idol_schedules = models.ManyToManyField(
        "idols.Schedule",
        blank=True,
        related_name="idols",
    )

    def str(self):
        return self.idol_name

    class Meta:
        verbose_name_plural = "Our_Idols"


class Schedule(CommonModel):
    """Schedule Model Definition"""

    ScheduleTitle = models.CharField(
        max_length=150,
        blank="",
        null=True,
    )

    ScheduleType = models.ForeignKey(
        "categories.Category",
        max_length=150,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="schedules",
    )

    participant = models.ManyToManyField(
        "idols.Idol",
        max_length=150,
        blank=True,
        related_name="schedules",
    )

    description = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name_plural = "Idol-Schedules"
