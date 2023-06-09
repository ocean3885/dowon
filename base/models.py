from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
from dowon import settings


class User(AbstractUser):
    phonnumber = models.CharField("전화번호", max_length=20, unique=True)


class Submit(models.Model):

    class Meta:
        ordering = ['-created']

    CATEGORY_CHOICES = [
        ("신생아작명", "신생아작명"),
        ("개명", "개명"),
        ("사주상담", "사주상담"),
        ("궁합", "궁합"),
        ("택일", "택일"),
    ]

    PROCESS_CHOICES = [
        ("입금대기", "입금대기"),
        ("진행중", "진행중"),
        ("완료", "완료"),
    ]

    VISIT_CHOICES = [
        ("방문상담", "방문상담"),
        ("전화상담", "전화상담"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    visit = models.CharField(max_length=20, choices=VISIT_CHOICES, null=True)
    wantdate = models.CharField(max_length=30, null=True)
    parents_name = models.CharField(max_length=25, blank=True)
    first_name_ch = models.CharField(max_length=25, blank=True)
    fav_name = models.CharField(max_length=100, blank=True)
    avoid_name = models.CharField(max_length=100, blank=True)
    adress = models.CharField(max_length=100, blank=True)
    phonnumber = models.CharField(max_length=20)
    email = models.EmailField(blank=True, max_length=254)
    description = models.TextField(blank=True)
    process = models.CharField(max_length=20, choices=PROCESS_CHOICES, null=True, default="입금대기")
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=50, blank=True)
    submit = models.ForeignKey(Submit, on_delete=models.CASCADE, related_name='persons')
    gen = models.CharField(max_length=1)
    sl = models.CharField(max_length=10)
    year = models.CharField(max_length=4)
    month = models.CharField(max_length=2)
    day = models.CharField(max_length=2)

    TIME_CHOICES = [
        ("子시 23:31~01:30", "子시 23:31~01:30"), ("丑시 01:31~03:30", "丑시 01:31~03:30"),
        ("寅시 03:31~05:30", "寅시 03:31~05:30"), ("卯시 05:31~07:30", "卯시 05:31~07:30"),
        ("辰시 07:31~09:30", "辰시 07:31~09:30"), ("巳시 09:31~11:30", "巳시 09:31~11:30"),
        ("午시 11:31~13:30", "午시 11:31~13:30"), ("未시 13:31~15:30", "未시 13:31~15:30"),
        ("申시 15:31~17:30", "申시 15:31~17:30"), ("酉시 17:31~19:30", "酉시 17:31~19:30"),
        ("戌시 19:31~21:30", "戌시 19:31~21:30"), ("亥시 21:31~23:30", "亥시 21:31~23:30"),
    ]
    time = models.CharField(max_length=25, choices=TIME_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

