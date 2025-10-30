import streamlit as st
with st.form('user_inputs'):
    age = st.number_input('年龄', min_value=0)
    sex = st.radio('性别', options=['男性','女性'])
    bmi = st.number_input('BMI', min_value=0.0)
    children = st.number_input("子女数量：",step=1, min_value=0)
    smoke = st.radio("是否抽烟", ("是","否"))
    region = st.selectbox('区域',('东南部', '西南部', '东北部', '西北部'))
    submitted = st.form_submit_button('预测费用')
if submitted:
    format_data = [age, sex, bmi, children, smoke, region]
    st.text(format_data)
sex_female, sex_male = 0, 0
if sex =='女性':
    sex_female = 1
elif sex == '男性':
    sex_male = 1
smoke_yes, smoke_no = 0, 0
if smoke == '是':
    smoke_yes = 1
elif smoke == '否':
    smoke_no = 1
region_northeast, region_southeast, region_northwest, region_southwest=0, 0, 0, 0
if region == '东北部':
    region_northeast = 1
elif region == '东南部':
    region_southeast = 1
elif region == '西北部':
    region_southwest = 1
elif region == '西南部':
    region_southwest = 1
st.write('转换为数据预处理的格式：')
format_data = [age, bmi, children, sex_female, sex_male, smoke_yes, smoke_no, region_northeast, region_southeast, region_northwest, region_southwest]
st.text(format_data)
