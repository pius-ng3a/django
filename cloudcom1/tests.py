from django.test import TestCase,SimpleTestCase

# Create your tests here.
#this class is used to test locally that code written does not voilate norms and can run on browser
class SimpleTests(TestCase):
	"""docstring for SimpleTests"""
	def homePageTest(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code,200)
	def aboutPageTest(self):
		response = self.response.get("/about/")
		self.assertEqual(response.status_code,200)
		