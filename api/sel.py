from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random
import time


def sel():
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("--remote-debugging-port=9222")

        user_agent_string = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        options.add_argument(f"user-agent={user_agent_string}")

        prefs = {
            "profile.managed_default_content_settings.images": 2,
            "profile.default_content_setting_values.css": 2,
        }
        options.add_experimental_option("prefs", prefs)

        paises = []

        for i in range(70):
            paises.append("mx")
        for i in range(15):
            paises.append("us")
        for i in range(5):
            paises.append("es")

        paises.extend(["ar", "co", "pe", "cl", "br", "ec", "gt", "cu", "do", "bo"])
        pais = random.choice(paises)

        proxy_options = {
            "proxy": {
                "http": f"http://customer-migruedav-cc-{pais}:Migruedav1234@pr.oxylabs.io:7777",
                "https": f"https://customer-migruedav-cc-{pais}:Migruedav1234@pr.oxylabs.io:7777",
                "no_proxy": "localhost,127.0.0.1",
            },
            "verify_ssl": True,
            "suppress_connection_errors": False,
        }

        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager(driver_version="123.0.6312.58").install()
            ),
            options=options,
            seleniumwire_options=proxy_options,
        )

        driver.get("https://www.youmainlyyou.com/")

        time.sleep(5)
        arts = driver.find_elements(by="css selector", value="a:has(img):has(h3)")
        cats = [
            "Wellbeing & Health",
            "Allure & Grooming",
            "Taste",
            "Style",
            "Bon Voyage",
            "Awareness",
            "Gadgets",
            "Furnishing",
        ]
        cat = driver.find_element(by="link text", value=random.choice(cats))
        print("cat", cat.text)
        cat.click()

        time.sleep(5)

        random_time = random.randint(1, 10)
        random_time = 3
        print("time1", random_time)
        time.sleep(5)
        arts = driver.find_elements(by="css selector", value="a:has(img):has(h3)")
        cats = [
            "Wellbeing & Health",
            "Allure & Grooming",
            "Taste",
            "Style",
            "Bon Voyage",
            "Awareness",
            "Gadgets",
            "Furnishing",
        ]
        cat = driver.find_element(by="link text", value=random.choice(cats))
        print("cat", cat.text)
        cat.click()
        # random_time = random.randint(1, 10)
        random_time = 3
        print("time2", random_time)
        time.sleep(5)
        arts = driver.find_elements(by="css selector", value="a:has(img):has(h3)")
        art = random.choice(arts)
        art.click()
        # random_time = random.randint(1, 10)
        random_time = 3
        print("time3", random_time)
        time.sleep(5)
        driver.quit()

        return {"pais": pais, "message": "METDC"}
    except Exception as e:
        return str(e)
