import streamlit as st
import requests

st.title('Genuine vs Misleading News detector')
news = st.text_area('Enter your news title here :',placeholder='E.g: Trump badmouthed Ukranian president')

API_URL='http://127.0.0.1:8889/result'

if st.button('Ask Model'):
    if news.strip():
        payload={
            'text':news
        }

        try:
            result = requests.post(API_URL, json=payload)
            if result.status_code == 200:
                result_data = result.json()
                st.subheader('Model response')
                st.markdown(f"**Final Response:** {result_data['Result']}")
            else:
                st.error(f'Error from server: {result.status_code}')
        except requests.exceptions.RequestException as e:
            st.error(f'Error connecting to API: {e}')

    else:
        st.warning('Kindly enter a news title.')

#Run following command in cmd:
#streamlit run frontend.py
