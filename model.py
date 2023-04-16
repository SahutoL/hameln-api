import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
}


urls = ["https://syosetu.org/?mode=rank_day",
        "https://syosetu.org/?mode=rank_week",
        "https://syosetu.org/?mode=rank_month",
        "https://syosetu.org/?mode=rank_3month",
        "https://syosetu.org/?mode=rank_year",
        "https://syosetu.org/?mode=rank_total"]

filter = ["日間", "週間", "月間", "四半期", "年間", "累計"]

def get_daily_novel():
    session = requests.Session()
    req = session.get(urls[0], headers=headers)
    elements = BeautifulSoup(req.text, "html.parser")
    daily_novels = main(elements, filter[0])
    return daily_novels

def get_weekly_novel():
    session = requests.Session()
    req = session.get(urls[1], headers=headers)
    elements = BeautifulSoup(req.text, "html.parser")
    weekly_novels = main(elements, filter[1])
    return weekly_novels

def get_monthly_novel():
    session = requests.Session()
    req = session.get(urls[2], headers=headers)
    elements = BeautifulSoup(req.text, "html.parser")
    return main(elements, filter[2])

def get_three_monthly_novel():
    session = requests.Session()
    req = session.get(urls[3], headers=headers)
    elements = BeautifulSoup(req.text, "html.parser")
    return main(elements, filter[3])

def get_yearly_novel():
    session = requests.Session()
    req = session.get(urls[4], headers=headers)
    elements = BeautifulSoup(req.text, "html.parser")
    return main(elements, filter[4])

def get_total_novel():
    session = requests.Session()
    req = session.get(urls[5], headers=headers)
    elements = BeautifulSoup(req.text, "html.parser")
    return main(elements, filter[5])


def main(elements, filter_name):
    titles, authors = list(), list()
    statuses, episodes, words = list(), list(), list()
    evaluations = list()
    ranks = list()
    parodies = list()
    update_days, update_times = list(), list()
    descriptions = list()
    alert_keywords, pre_keywords, keywords = list(), list(), list()
    blank = [""]
    novels = dict()
    for i in elements.find_all("div", class_="blo_title_base"):
        titles.append(i.find("b").get_text().replace("\n", "").replace("\u3000", ""))
        authors.append(i.find("div", class_="blo_title_sak").get_text().replace("\n", "").replace("\u3000", "").replace("作：", ""))

    for i in elements.find_all("div", class_="blo_wasuu_base"):
        statuses.append(i.find("span").get_text())
        episodes.append(int(i.find("b").get_text()))
        words.append(int(i.find("div").get_text().replace(",", "").replace(" 字", "")))

    for i in elements.find_all("div", class_="blo_hyouka"):
        evaluations.append(float(i.find(class_="blo_mix").get_text().replace("調整平均：", "")))

    for i in elements.find_all("span", class_="blo_rank"):
        ranks.append(i.get_text())

    for i in elements.find_all("div", class_="blo_genre"):
        parodies.append(i.get_text())

    for i in elements.find_all("div", class_="blo_date"):
        update_days.append(i.get_text()[:10])
        update_times.append(i.find("div").get_text())

    for i in elements.find_all("div", class_="blo_inword"):
        descriptions.append(i.get_text())

    for i in elements.find_all("span", class_="alert_color"):
        alert_keywords.append(i.get_text().split(" ")[:-1])

    for i in elements.find_all("div", class_="all_keyword"):
        if "./?mode=review&" in i.find("a").get("href"):
            continue
        pre_keywords.append(i.get_text().split(" ")[:-1])

    for i in range(len(titles)):
        keywords.append(list(set(alert_keywords[i]) ^ set(pre_keywords[i]) ^ set(blank)))


    for i in range(len(titles)):
        novels[i+1] = {
            "{}ランキング".format(filter_name): ranks[i],
            "作品名": titles[i],
            "著者": authors[i],
            "ジャンル": parodies[i],
            "状態": statuses[i],
            "話数": episodes[i],
            "総文字数": words[i],
            "詳細": descriptions[i],
            "警告タグ": alert_keywords[i],
            "タグ": keywords[i],
            "平均評価": evaluations[i],
            "更新日": update_days[i],
            "更新時": update_times[i],
        }
    return novels
