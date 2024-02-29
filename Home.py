import streamlit as st
import httpx


def query_ui():
    filters = {
        "日間": "day",
        "週間": "week",
        "月間": "month",
        "四半期": "3month",
        "年間": "year",
        "総合": "total",
    }

    filter = st.selectbox('',(list(filters.keys())))
    st.write('')

    return filters, filter


def main():
    st.markdown('## ハーメルンランキング')

    filters, filter= query_ui()

    if st.button("データ取得"):
        print(filters[filter])
        response = httpx.get(f'https://hameln-api.onrender.com/ranking/?filter={filters[filter]}')

        res = response.json()
        st.write('')
        st.json(res)

if __name__ == '__main__':
    main()
