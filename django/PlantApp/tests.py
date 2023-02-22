from django.test import TestCase, SimpleTestCase
from PlantApp.models import Plant


class SimpleTest(TestCase):

    def setUp(self):
        Plant.objects.create(name='cactusTest', born_in='2023-01-25', color='verde', size='S', heigth=0,
                                          width=0, level=1, water=25, humidity=25, sunlight=30, nutrients=50,
                                          last_time_watered='2023-01-26', last_time_fertilised='2023-01-26')

    def test_create_plant_object_db(self):
        plant_test = Plant.objects.filter(name='cactusTest')[0]
        self.assertIsNotNone(plant_test)

    def test_create_plant_object(self):
        plant_test = Plant(name="cactusTestObject", color="green", size="XS", heigth=0, width=0)
        self.assertIsNotNone(plant_test)

    def test_print_plant(self):
        plant_test = Plant.objects.filter(name='cactusTest')[0]
        self.assertEqual(str(plant_test), "cactusTest is at level: 1")

    def test_delete_plant_db(self):
        plant_test = Plant.objects.filter(name="cactusTest")[0]
        plant_test.delete()
        plant_test_count = Plant.objects.filter(name="cactusTest").count()
        self.assertEqual(0, plant_test_count)

    def water_plant(self):
        pass