import time
import unittest
import ddt
from selenium import webdriver
from selenium.webdriver.common.by import By
from excel_util import ExcelUtil
@ddt.ddt()
class TestDemo(unittest.TestCase):
    eu = ExcelUtil()
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        