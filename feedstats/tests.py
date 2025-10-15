import pytest
from .models import SubscriberCount
import datetime


@pytest.mark.django_db
class TestFeedstats:
    def test_feedstats_records_subscriber_numbers(self, client):
        assert SubscriberCount.objects.count() == 0
        # If no \d+ subscribers, we don't record anything
        client.get("/atom/everything/", HTTP_USER_AGENT="Blah")
        assert SubscriberCount.objects.count() == 0
        client.get("/atom/everything/", HTTP_USER_AGENT="Blah (10 subscribers)")
        assert SubscriberCount.objects.count() == 1
        row = SubscriberCount.objects.all()[0]
        assert row.path == "/atom/everything/"
        assert row.count == 10
        assert row.created.date() == datetime.date.today()
        assert row.user_agent == "Blah (X subscribers)"
        # If we hit again with the same number, no new record is recorded
        client.get("/atom/everything/", HTTP_USER_AGENT="Blah (10 subscribers)")
        assert SubscriberCount.objects.count() == 1
        # If we hit again with a different number, we record a new row
        client.get("/atom/everything/", HTTP_USER_AGENT="Blah (11 subscribers)")
        assert SubscriberCount.objects.count() == 2
        row = SubscriberCount.objects.all()[1]
        assert row.count == 11
        assert row.user_agent == "Blah (X subscribers)"
