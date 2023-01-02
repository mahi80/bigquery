from datetime import date
from unittest.mock import patch
from django.test import TestCase

from app.views import update
 
def mocked_today():
    return date(year=2020, month=1, day=1)
 
class TestImmutableObject(TestCase):
    @patch("app.views.update", mocked_today)
    def test_myfunc_using_date(self):
        self.assertEqual(update(self,12,13).status_code, 200)