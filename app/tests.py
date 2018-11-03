from django.test import TestCase
import datetime
import pytz

from django.db.models.functions import *
from django.utils import timezone

from app.models import TimeStampModel
from app.data import make_timestamp_data

# Create your tests here.

class Ticket29884Test(TestCase):

    def setUp(self):
        make_timestamp_data()

    def find(self):
        queryset = TimeStampModel.objects.annotate(
            day=TruncDay('timestamp', tzinfo=pytz.timezone('Europe/Berlin'))
        ).filter(
            day=timezone.make_aware(datetime.datetime(2018, 10, 24), pytz.timezone('Europe/Berlin'))
        ).values()
        results = list(queryset)
        self.assertGreater(len(results), 0) 

    def test_find(self):
        self.find()