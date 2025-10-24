import streamlit as st
st.set_page_config(page_title='视频',page_icon='📺︎')
video_file = 'tv/trailer.mp4'

st.subheader('展示视频')
st.video(video_file)
