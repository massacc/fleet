from django.test import TestCase
from .models import Registration
from .forms import RegistrationForm
from datetime import date
from datetime import timedelta
from django.core.exceptions import ValidationError

class VehicleTestCase(TestCase):

    pass

class RegistrationTestCase(TestCase):
    def test_date_not_in_future(self):
        future = date.today() + timedelta(days=1)
        with self.assertRaises(ValidationError):
            registration = Registration.objects.create(plate='TEST_PLATE', start_date=future)
            registration.full_clean()

class RegistraionFormTestCase(TestCase):
    def test_deregistration_before_registration(self):
        dereg_date = date.today() 
        reg_date = date.today() + timedelta(days=1)

        registration_form = RegistrationForm({
                            'plate':'test', 
                            'start_date':reg_date, 
                            'end_date':dereg_date
        })
        
        self.assertFalse(registration_form.is_valid())

