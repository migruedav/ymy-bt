from scrapingbee import ScrapingBeeClient
import random

client = ScrapingBeeClient(
    api_key="MG7MAQYR4SH3ZAVORYCUZODTXPKTCJ47C2JV8V4IG2SGUO9ETU1Q3PJDJ3QTIJWFWCIERVHFP6P8DGKM"
)

cat = random.choice(
    ["#cat1", "#cat2", "#cat3", "#cat4", "#cat5", "#cat6", "#cat7", "#cat8"]
)
art = random.choice(["#art1", "#art2", "#art3", "#art4", "#art5", "#art6"])


def bee():
    js_scenario = {
        "instructions": [
            {"wait": 3000},
            {"click": cat},
            {"wait": 3000},
            {"click": art},
            {"wait": 3000},
        ]
    }

    response = client.get(
        "https://www.youmainlyyou.com/",
        params={
            "premium_proxy": "true",
            "js_scenario": js_scenario,
            "country_code": "cr",
        },
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
        },
    )
    print("Response HTTP Status Code: ", response.status_code)
    print("Response HTTP Response Body: ", response.content)

    return "Visita exitosa desde Costa Rica"
