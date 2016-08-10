from selenium import webdriver
from django.test import LiveServerTestCase

class FunctionalTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test(self):
        self.assertEqual(1, 2)
