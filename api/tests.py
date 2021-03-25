from django.test import TestCase
from api.models import Person, Address, Email, Mobile


# Models Related unit test cases
class PersonTest(TestCase):

    def record_person_details(self, name="Anonymous"):
        return Person.objects.create(name=name)

    def test_record_person_details(self):
        w = self.record_person_details()
        self.assertTrue(isinstance(w, Person))
        self.assertEqual(w.name, 'Anonymous')
