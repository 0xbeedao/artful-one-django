import pytest
import os
import django
from django.conf import settings
from django.test import Client


def pytest_configure():
    """Configure Django for pytest."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    if not settings.configured:
        django.setup()


@pytest.fixture
def client():
    """Django test client fixture."""
    return Client()
