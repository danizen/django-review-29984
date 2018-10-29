from django.test import TestCase
import pytz

from app.models import TimeStampModel

# Create your tests here.

class Ticket29884Test(TestCase):

    def setUp(self):
        TimeStampModel.objects.bulk_create([
            TimeStampModel(timestamp=datetime.datetime(2018, 10, 24, 5, 13, tzinfo=pytz.utc)),
            TimeStampModel(timestamp=datetime.datetime(2018, 10, 24, 7, 4, tzinfo=pytz.utc)),
            TimeStampModel(timestamp=datetime.datetime(2018, 10, 24, 8, 56, tzinfo=pytz.utc)),
            TimeStampModel(timestamp=datetime.datetime(2018, 10, 24, 13, 49, tzinfo=pytz.utc)),
            TimeStampModel(timestamp=datetime.datetime(2018, 10, 24, 15, 33, tzinfo=pytz.utc)),
            TimeStampModel(timestamp=datetime.datetime(2018, 10, 24, 18, 29, tzinfo=pytz.utc)),
            TimeStampModel(timestamp=datetime.datetime(2018, 10, 24, 19, 12, tzinfo=pytz.utc)),
            TimeStampModel(timestamp=datetime.datetime(2018, 10, 24, 21, 37, tzinfo=pytz.utc)),
            TimeStampModel(timestamp=datetime.datetime(2018, 10, 24, 21, 9, tzinfo=pytz.utc)),
            TimeStampModel(timestamp=datetime.datetime(2018, 10, 24, 23, 23, tzinfo=pytz.utc)),
        ])

    def test_find(self):
