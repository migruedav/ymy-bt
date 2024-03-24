from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def sel():
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.binary_location = "/usr/bin/"

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )

        url = "https://redis.com/"

        driver.get(url)
        return driver.title
    except Exception as e:
        return str(e)
