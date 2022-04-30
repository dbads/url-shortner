import json
from django.test import TestCase
from .models import Url
from .views import shorten, get_url
from django.test.client import RequestFactory


class UrlGetUrl(TestCase):
    def setUp(self):
        Url.objects.create(actual="test url", shortcode="shortcode")
        self.factory = RequestFactory()

    def test_get_url_with_valid_shortcode(self):
        request = self.factory.get('/get-url/shortcode')
        response = json.loads(get_url(request, 'shortcode').content)
        self.assertEqual(response["location"], 'test url')
    
    def test_get_url_with_invalid_shortcode(self):
        request = self.factory.get('/get-url/shortcodeinvalid')
        response = get_url(request, 'shortcodeinvalid')
        self.assertEqual(response.status_code, 404)
