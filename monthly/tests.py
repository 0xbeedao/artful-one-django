import pytest
from datetime import datetime

from django.urls import reverse
from django.utils import timezone

from .models import Newsletter


@pytest.mark.django_db
class TestMonthlyViews:
    @pytest.fixture(autouse=True)
    def setup_newsletters(self):
        self.newsletter_old = Newsletter.objects.create(
            subject="Older edition",
            body="Old body",
            sent_at=timezone.make_aware(datetime(2024, 1, 31, 12, 0, 0)),
        )
        self.newsletter_new = Newsletter.objects.create(
            subject="Newer edition",
            body="New **body**",
            sent_at=timezone.make_aware(datetime(2024, 2, 29, 12, 0, 0)),
        )

    def test_monthly_index_lists_newsletters(self, client):
        response = client.get(reverse("monthly:index"))
        assert response.status_code == 200
        newsletters = list(response.context["newsletters"])
        assert newsletters == [self.newsletter_new, self.newsletter_old]
        assert "Newer edition" in response.content.decode()
        assert "Older edition" in response.content.decode()
        assert (
            reverse("monthly:detail", kwargs={"year": 2024, "month": "02"})
            in response.content.decode()
        )

    def test_newsletter_detail_renders_content(self, client):
        response = client.get(
            reverse("monthly:detail", kwargs={"year": 2024, "month": "02"})
        )
        assert response.status_code == 200
        assert response.context["newsletter"] == self.newsletter_new
        assert "Newer edition" in response.content.decode()
        assert "<strong>body</strong>" in response.content.decode()

    def test_newsletter_detail_missing(self, client):
        response = client.get(
            reverse("monthly:detail", kwargs={"year": 2023, "month": "12"})
        )
        assert response.status_code == 404
