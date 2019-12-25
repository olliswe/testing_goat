from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('http://localhost:8000')

assert 'Django' in browser.title
