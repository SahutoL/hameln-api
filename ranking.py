import requests
import bs4
from time import sleep

class Ranking():
    def hameln_ranking(self, filter):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        }

        session = requests.Session()
        page_number = 1
        search_url = 'https://syosetu.org/?mode=rank_{}'.format(filter)
        
        sleep(1)
        req = session.get(search_url, headers=headers)

        elements = bs4.BeautifulSoup(req.text, "html.parser")
        parsed_page = elements.select('div.section3')

        items = []
        rank = 1
        for _ in range(1):
            for site in parsed_page:
                if site.find(attrs={'title': "最新話へのリンク"}).get_text() == "": continue
                number_aleart_keyword = len(site.find("span", class_="alert_color").get_text().split(" ")[:-1])
                item = {
                    '順位': rank,
                    '作品名': site.find('div', class_="blo_title_base").find("b").get_text().replace("\n", "").replace("\u3000", ""),
                    '作者': site.find("div", class_="blo_title_sak").get_text().replace("\n", "").replace("\u3000", "").replace("作：", ""),
                    "原作": site.find("div", class_="blo_genre").get_text().replace("\n", "").replace("原作：","")[1:-1],
                    "状態": site.find("div", class_="blo_wasuu_base").find("span").get_text(),
                    "話数": int(site.find(attrs={'title': "最新話へのリンク"}).get_text()),
                    "総文字数": int(site.find(attrs={'title': "総文字数"}).get_text().replace(",", "").replace("全 ", "").replace(" 字", "")),
                    "詳細": site.find("div", class_="blo_inword").get_text().replace("\u3000",""),
                    "警告タグ": site.find("span", class_="alert_color").get_text().split(" ")[:-1],
                    "タグ": site.find("div", class_="all_keyword").get_text().split(" ")[number_aleart_keyword+1:-1],
                    "平均評価": float(site.find("div", class_="blo_hyouka").find(class_="blo_mix").get_text().replace("調整平均：", "")),
                    "更新日": site.find("div", class_="blo_date").get_text()[:10],
                    "更新時": site.find("div", class_="blo_date").find("div").get_text(),
                    "URL": "https:{}".format(site.find("div", class_="blo_title_base").find("a").get("href"))
                }
                rank += 1
                items.append(item)
            sleep(1)
            page_number += 1
            search_url = 'https://syosetu.org/search/?word={search_keyword}&page={page_number}&gensaku=原作：{search_gensaku}&type={search_type}'
            req = session.get(search_url, headers=headers)
            elements = bs4.BeautifulSoup(req.text, "html.parser")
            parsed_page = elements.select('div.section3')

        return items
