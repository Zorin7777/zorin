import streamlit as st

st.set_page_config(page_title='音乐',page_icon='🎶')
# 读取音频URL
music = [{'url':'https://music.163.com/song/media/outer/url?id=5260311.mp3',
               'photo':'https://p1.music.126.net/Oix4KKx3qsuL8UGiLKcDiA==/43980465127856.jpg?param=180y180',
               'name':'葡萄成熟时',
               'author':'陈奕迅'},
         {'url':'https://music.163.com/song/media/outer/url?id=2613686702.mp3',
          'photo':'https://p2.music.126.net/p6uM4LOzKh-b3r1eTmvU4g==/109951169838608004.jpg?param=180y180',
          'name':'孤单心事(DJ阿智Remix)',
          'author':'DJ阿智'},
         {'url':'https://music.163.com/song/media/outer/url?id=1834268297.mp3',
          'photo':'https://p2.music.126.net/gJpeTMYWBBXFXq7vpxmLxg==/109951165854197528.jpg?param=180y180',
          'name':'心墙',
          'author':'DJ.Mr.李'}]
         

if 'tp' not in st.session_state:
    st.session_state['tp'] = 0


 


a1,a2 = st.columns([1,2])
with a1:
    st.image(music[st.session_state['tp']]['photo'])
    st.text('封面专辑')
with a2:
    st.title(music[st.session_state['tp']]['name'])
    st.text(music[st.session_state['tp']]['author'])
def nextImg():
    st.session_state['tp'] = (st.session_state['tp'] + 1) % len(music)
def prevImg():
    st.session_state['tp'] = (st.session_state['tp'] - 1) % len(music)

st.audio(music[st.session_state['tp']]['url'])
b1,b2 = st.columns(2)
with b1:
    st.button('上一首', on_click=prevImg,use_container_width=True)
with b2:
    st.button('下一首', on_click=prevImg,use_container_width=True)
