from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed
from django.db.models import Value, TextField
from django.db import transaction, connection
from blog.models import BaseModel, Tag
import operator
from functools import reduce


@receiver(post_save)
def on_save(sender, **kwargs):
    pass


@receiver(m2m_changed)
def on_m2m_changed(sender, **kwargs):
    pass
