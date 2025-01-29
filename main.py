from bs4 import BeautifulSoup
import requests
import lxml
from fake_useragent import UserAgent
import json

#-------------------------------------------------------------------
# СОХРАНИЛА СТРАНИЦУ, ЧТОБ НЕ ДУДОСИТЬ САЙТ БЕСКОНЕЧНЫМИ ЗАПРОСАМИ
# ua = UserAgent()
#
# headers = {
#     "Accept": "*/*",
#     "User-Agent" : ua.random
# }

# req = requests.get(url="http://www.world-art.ru/animation/rating_top.php",
#                    headers=headers)
#
# src = req.text

# with open("word-art.html", "w", encoding="utf-8") as file:
#     file.write(src)
#-------------------------------------------------------------------
#ИЗ СОХРАНЕННОЙ СТРАНИЦЫ С ПОМОЩЬЮ ПАРСЕРА СОБИРАЮ ССЫЛКИ И НАЗВАНИЯ АНИМЕ С 1 СТРАНИЦЫ РЕЙТИНГА
# with open("word-art.html", "r", encoding="utf-8") as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, "lxml")
# hrefs = soup.find_all("a", class_="review")
#
#
# all_anime_dict = {}
#
# for item in hrefs:
#     item_href = item.get("href")
#
#     if "votes_history" not in item_href and "limit_" not in item_href:
        # item_text = item.text
        # # print(item_text, "___", item_href, end="\n\n")
        # all_anime_dict[item_text] = item_href
#
# with open("anime.json", "w", encoding="utf-8") as file:
#     json.dump(all_anime_dict, file, indent=4, ensure_ascii=False)
# ---------------------------------------------------------------------------
#ТЕПЕРЬ ХОЧУ ПРОЙТИСЬ ПО ПЕРВЫМ 5 СТРАНИЦАМ РЕЙТИНГА И ДОБАВИТЬ АНИМЕ В СПИСОК ФАЙЛА anime.json
#В СПИСКЕ >2000 АНИМЕПОЭТОМУ ОГРАНИЧУСЬ ПЕРВЫМИ 500 ШТ.


ua = UserAgent()

headers = {
    "Accept": "*/*",
    "User-Agent" : ua.random
}

limit1 = 0
limit2 = 100

all_anime_dict = {}
for _ in range(5):
    url = f"http://www.world-art.ru/animation/rating_top.php?limit_1={limit1}&limit_2={limit2}"
    req = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(req.text, "lxml")
    hrefs = soup.find_all("a", class_="review")

    for item in hrefs:
        item_href = item.get("href")

        if "votes_history" not in item_href and "limit_" not in item_href:
            item_text = item.text
            if item_text not in all_anime_dict.keys():
                all_anime_dict[item_text] = item_href

    limit1 += 100
    limit2 += 100

with open("anime.json", "w", encoding="utf-8") as file:
    json.dump(all_anime_dict, file, indent=4, ensure_ascii=False)