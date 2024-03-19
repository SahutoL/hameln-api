import streamlit as st
from streamlit_option_menu import option_menu
import httpx
import urllib.parse

st.set_page_config(
    initial_sidebar_state="collapsed"
)


def query_ui():
    parodies = [
        "--原作カテゴリ--",
        "その他原作",
        "二次創作",
        "オリジナル",
        "ARMORED CORE",
        "BanG Dream!",
        "BLEACH",
        "FAIRY TAIL",
        "Fate/",
        "GOD EATER",
        "HUNTER×HUNTER",
        "Infinite Dendrogram",
        "Muv-Luv",
        "NARUTO",
        "NEW GAME!",
        "ONE PIECE",
        "Re:ゼロから始める異世界生活",
        "VOICEROID",
        "アークナイツ",
        "アイドルマスター",
        "アカメが斬る!",
        "アクタージュ",
        "アサルトリリィ",
        "アズールレーン",
        "ありふれた職業で世界最強",
        "暗殺教室",
        "痛いのは嫌なので防御力に極振りしたいと思います。",
        "イナズマイレブン",
        "インフィニット・ストラトス",
        "ウルトラマン",
        "ウマ娘プリティーダービー",
        "英雄伝説",
        "オーバーロード",
        "推しの子",
        "ガールズ＆パンツァー",
        "学戦都市アスタリスク",
        "かぐや様は告らせたい",
        "陰の実力者になりたくて！",
        "がっこうぐらし！",
        "家庭教師ヒットマンREBORN!",
        "仮面ライダー",
        "艦隊これくしょん",
        "ガンダム",
        "カンピオーネ！",
        "鬼滅の刃",
        "銀河英雄伝説",
        "蜘蛛ですが、なにか？",
        "グランブルーファンタジー",
        "ゲート 自衛隊 彼の地にて、斯く戦えり",
        "けものフレンズ",
        "原神",
        "恋姫†無双",
        "コードギアス",
        "ご注文はうさぎですか？",
        "五等分の花嫁",
        "この素晴らしい世界に祝福を！",
        "ゴブリンスレイヤー",
        "咲-Saki-",
        "シャングリラ・フロンティア",
        "呪術廻戦",
        "食戟のソーマ",
        "ジョジョの奇妙な冒険",
        "進撃の巨人",
        "新世紀エヴァンゲリオン",
        "スーパーロボット大戦",
        "ストライクウィッチーズ",
        "ストライク・ザ・ブラッド",
        "ゼロの使い魔",
        "戦姫絶唱シンフォギア",
        "ソードアート・オンライン",
        "葬送のフリーレン",
        "ダイの大冒険",
        "対魔忍",
        "盾の勇者の成り上がり",
        "ダンガンロンパ",
        "ダンジョンに出会いを求めるのは間違っているだろうか",
        "チェンソーマン",
        "超次元ゲイムネプテューヌ",
        "デート・ア・ライブ",
        "テイルズオブ",
        "転生したらスライムだった件",
        "ドールズフロントライン",
        "とある魔術の禁書目録",
        "東京喰種",
        "東方Project",
        "刀使ノ巫女",
        "ドラゴンクエスト",
        "ドラゴンボール",
        "ニセコイ",
        "日本国召喚",
        "バイオハザード",
        "ハイスクールD×D",
        "ハイスクール・フリート",
        "ハイキュー!!",
        "バカとテストと召喚獣",
        "ハリー・ポッター",
        "緋弾のアリア",
        "ファイアーエムブレム",
        "プリキュア",
        "プリンセスコネクト！Re:Dive",
        "ブルーアーカイブ",
        "ブルーロック",
        "プロジェクトセカイ",
        "ペルソナ",
        "僕のヒーローアカデミア",
        "ポケットモンスター",
        "ぼっち・ざ・ろっく！",
        "真剣で私に恋しなさい!",
        "魔法科高校の劣等生",
        "魔法少女まどか☆マギカ",
        "魔法少女リリカルなのは",
        "魔法先生ネギま！",
        "無職転生",
        "名探偵コナン",
        "メイドインアビス",
        "女神転生",
        "モンスターハンター",
        "問題児たちが異世界から来るそうですよ？",
        "やはり俺の青春ラブコメはまちがっている。",
        "遊戯王",
        "結城友奈は勇者である",
        "ゆるキャン△",
        "ようこそ実力至上主義の教室へ",
        "幼女戦記",
        "落第騎士の英雄譚",
        "ラブライブ！",
        "ランスシリーズ",
        "リコリス・リコイル",
        "りゅうおうのおしごと！",
        "ロクでなし魔術講師と禁忌教典",
        "ワールドトリガー",
    ]
    sorts = [
        "最終更新日時(新しい順)",
        "最終更新日時(古い順)",
        "総合評価 ",
        "通算UA数(多い順)",
        "通算UA数(少ない順)",
        "平均評価(高い順)",
        "平均評価(低い順)",
        "加重平均(高い順)",
        "加重平均(低い順)",
        "1話あたりの文字数(多い順)",
        "1話あたりの文字数(少ない順)",
        "初回投稿日(新しい順)",
        "初回投稿日(古い順)",
        "お気に入り数(多い順)",
        "お気に入り数(少ない順)",
        "しおり数(多い順)",
        "しおり数(少ない順)",
        "ここすき数(多い順)",
        "ここすき数(少ない順)",
        "今週UA数(多い順)",
        "今週UA数(少ない順)",
        "先週UA数(多い順)",
        "先週UA数(少ない順)",
        "投票者数(多い順)",
        "投票者数(少ない順)",
        "総評価数(多い順)",
        "総評価数(少ない順)",
        "総文字数(多い順)",
        "総文字数(少ない順)",
        "感想数(多い順)",
        "感想数(少ない順)",
        "話数(多い順)",
        "話数(少ない順)",
        "中央値(高い順)",
        "中央値(低い順)",
        "日間総合評価",
        "週間総合評価",
        "月間総合評価",
        "四半期総合評価",
        "年間総合評価",
        "Wilson Score Interval",
        "相対評価",
        "ピックアップ(総合評価/UA)",
        "ランダム"
    ]

    input_word = st.text_input(label='キーワード入力', value='')
    st.write('')
    parody = st.selectbox('原作',(parodies),placeholder="原作カテゴリを選択してください")
    st.write('')
    sort = st.selectbox('並び替え', (sorts))
    st.write('')
    st.write('')

    return input_word, parody, sort


def main():
    changed = option_menu(None, ["Home", "Search"],
        icons=['house', 'search'],
        orientation="horizontal",
        default_index=1)
    
    if changed == "Home":
        st.switch_page('Home.py')
    
    st.markdown('## ハーメルン検索')

    input_word, parody, sort = query_ui()

    if st.button("データ取得"):
        with httpx.Client(timeout=httpx.Timeout(None)) as client:
            if input_word == "": input_word = " "
            response = client.get(f'https://hameln-api.onrender.com/search/?search_word={input_word}&gensaku={parody}&sort={sort}')

        res = response.json()
        st.write('')
        st.code("""
            curl -X \'GET\' \\
              \'https://hameln-api.onrender.com/search/?search_word={}&gensaku={}&sort={}' \\
              -H \'accept: application/json\'
        """.format(urllib.parse.quote(input_word), urllib.parse.quote(parody), urllib.parse.quote(sort)))
        st.write('')
        st.json(res)

if __name__ == '__main__':
    main()
