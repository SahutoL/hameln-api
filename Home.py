import streamlit as st
from streamlit_option_menu import option_menu
import httpx

st.set_page_config(
    initial_sidebar_state="collapsed"
)

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

    changed = option_menu(None, ["Home", "Search"],
        icons=['house', 'search'],
        orientation="horizontal",
        default_index=0)
    
    if changed == "Search":
        st.switch_page('pages/Search.py')
        
    
    
    
    st.markdown('## ハーメルンランキング')
    filters, filter= query_ui()

    if st.button("データ取得"):
        with httpx.Client(timeout=httpx.Timeout(None)) as client:
            response = client.get(f'https://hameln-api.onrender.com/ranking/?filter={filters[filter]}')

        res = response.json()
        st.write('')
        st.code("""
            curl -X \'GET\' \\
            \'https://hameln-api.onrender.com/ranking/?filter=' \\
            -H \'accept: application/json\'
        """.format({filters[filter]}))
        st.write('')
        st.json(res)

if __name__ == '__main__':
    main()
