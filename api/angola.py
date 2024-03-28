from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import time
from webdriver_manager.chrome import ChromeDriverManager


def angola():
    username = "spm0uynyl7"
    password = "2ydXJhdsyHyCi_78s8"
    proxy = f"http://{username}:{password}@ao.smartproxy.com:18000"

    options = {
        "proxy": {
            "http": proxy,
            "https": proxy,
            "no_proxy": "localhost,127.0.0.1",
        }
    }

    prefs = {
        "profile.managed_default_content_settings.images": 2,
    }

    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    )

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager(driver_version="123.0.6312.58").install()),
        seleniumwire_options=options,
        options=chrome_options,
    )

    driver.get("https://www.youmainlyyou.com")
    time.sleep(20)
    btn = driver.find_element(by="link text", value="Taste")
    btn.click()
    time.sleep(5)
    driver.quit()

    return "Visita exitosa desde Angola"
