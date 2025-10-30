import streamlit as st
import pickle
import pandas as pd
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
    format_data = [age, bmi, children, sex_female, sex_male, smoke_yes, smoke_no, region_northeast, region_southeast, region_northwest, region_southwest]
with open('rfr_model.pkl','rb') as f:
    rfr_model = pickle.load(f)
if submitted:
    format_data_df = pd.DataFrame(data=[format_data], columns=rfr_model.feature_names_in_)
    predict_result = rfr_model.predict(format_data_df)[0]
    st.write('根据您输入的数据，预测该客户的医疗费用是：', round(predict_result,2))

    
