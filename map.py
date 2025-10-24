import streamlit as st
import pandas as pd
map_data = {
    'latitude':[22.854160, 22.840392, 22.838409, 22.841667, 22.847446],
    'longitude':[108.222322, 108.245341, 108.217607, 108.245700, 108.220922],
    }
st.map(pd.DataFrame(map_data))



import streamlit as st
import pandas as pd

# 定义数据,以便创建数据框
data = {
    '1号门店':[200, 150, 180],
    '2号门店':[120, 160, 123],
    '3号门店':[110, 100, 160],
}
df = pd.DataFrame(data)
index = pd.Series(["1月""2月""3月"], name='月份')
st.area_chart(df)
