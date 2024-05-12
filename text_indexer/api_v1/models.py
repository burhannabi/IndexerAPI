from datetime import datetime, date
from uuid import UUID
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    id: UUID = models.AutoField(primary_key=True)
    name: str = models.CharField(max_length=150, null=False)
    email: str = models.EmailField(
        _('email_address'),
        max_length=256, unique=True,
        null=False
    )
    dob: date = models.DateField(_('date_of_birth'), null=False)
    created_at: datetime = models.DateTimeField(auto_now_add=True)
    modified_at: datetime = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.email


class Paragraph(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()

    def __str__(self):
        return f"Paragraph: {self.id[:6]}"


class WordIndex(models.Model):
    word = models.CharField(max_length=255)
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE)

    class Meta:
        # ensures a unique combination of word and paragraph
        unique_together = (("word", "paragraph"),)

    def __str__(self):
        return f"Word: {self.word}, Paragraph: {self.paragraph.id[:6]}"
