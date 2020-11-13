import unittest
import requests


class Fake(unittest.TestCase):

    def test_0(self):
        url = "http://192.168.1.84:5000/ingredient"
        response = requests.get(url, verify=False)
        response_body = response.json()
        print(response_body)

    def test_1(self):
        url = "http://192.168.1.84:5000/ingredient"
        body = {"name": "test_ingredient_romain",
                "slug": "test_ingredient_romain_slug"}
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        print(response_body)
