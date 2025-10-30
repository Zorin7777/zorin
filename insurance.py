import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
insurance_df = pd.read_csv(r'D:/streamlit_env/（医疗费用预测数据）insurance-chinese.csv', encoding='gbk')
print("输出数据框的前5行记录，如下")
print(insurance_df.head())
print()

print("输出数据框的各列的详细信息如下：")
insurance_df.info()
