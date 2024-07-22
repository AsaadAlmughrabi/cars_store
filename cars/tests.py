from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Car

class CarTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test_user',
            email="test@email.com",
            password="1234"
        )

        self.car = Car.objects.create(
            buyer=self.user,
            model="test_model",
            brand="test_brand",
            price=10000,
            is_bought=True,
            buy_time="2024-07-20 10:00:00"
        )

    def test_list_page_status_code(self):
        url = reverse('cars')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('cars')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'cars.html')
        self.assertTemplateUsed(response, 'base.html')

    def __str__(self):
        return self.model
        

    def test_details_view(self):
        url = reverse('car_detail', args=[self.car.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'car_detail.html')

    def test_create_view(self):
        data = {
            "buyer": self.user.id,
            "model": "test_model_2",
            "brand": "test_brand_2",
            "price": 15000,
            "is_bought": False,
            "buy_time": "2024-07-20 12:00:00"
        }

        url = reverse('car_create')
        response = self.client.post(path=url, data=data, follow=True)
        self.assertEqual(len(Car.objects.all()), 2)
        new_car = Car.objects.get(model="test_model_2")
        self.assertRedirects(response, reverse('car_detail', args=[new_car.id]))

    def test_update_view(self):
        data = {
            "buyer": self.user.id,
            "model": "updated_model",
            "brand": "updated_brand",
            "price": 20000,
            "is_bought": True,
            "buy_time": "2024-07-20 14:00:00"
        }

        url = reverse('car_update', args=[self.car.id])
        response = self.client.post(path=url, data=data, follow=True)
        self.car.refresh_from_db()
        self.assertEqual(self.car.model, "updated_model")
        self.assertRedirects(response, reverse('car_detail', args=[self.car.id]))

    def test_delete_view(self):
        url = reverse('car_delete', args=[self.car.id])
        response = self.client.post(path=url, follow=True)
        self.assertEqual(Car.objects.count(), 0)
        self.assertRedirects(response, reverse('cars'))
