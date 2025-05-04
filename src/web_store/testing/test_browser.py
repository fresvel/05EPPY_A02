import unittest
from selenium import webdriver

class TestBrowser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the Chrome WebDriver
        options = webdriver.ChromeOptions()
        options.binary_location = "/home/fresvel/Documentos/Capacitación/Python/Viu/Librerías_y_Proyectos/Actividades/05EPPY_A01/src/chrome-linux/chrome"  
        cls.driver = webdriver.Chrome(options)
        cls.driver.get("http://localhost:8000")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    


    def setUp(self):
        # Set up the Chrome WebDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()

    def test_open_browser(self):
        # Open a URL and check the title
        self.driver.get("https://www.example.com")
        self.assertIn("Example Domain", self.driver.title)

    def test_navigate_to_page(self):
        # Navigate to a page and check the URL
        self.driver.get("https://www.example.com")
        self.assertEqual(self.driver.current_url, "https://www.example.com/")