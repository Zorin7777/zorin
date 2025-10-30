import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
insurance_df = pd.read_csv(r'D:/streamlit_env/（医疗费用预测数据）insurance-chinese.csv', encoding='gbk')
output = insurance_df['医疗费用']
features = insurance_df[['年龄','性别','BMI','子女数量','是否吸烟','区域']]
features = pd.get_dummies(features)
print('下面是独热编码后，特征列的前5行数据：')
print(features.head())
print()
print("前5行目标输出数据")
print(output.head())
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
pd.set_option('display.unicode.east.asian_width','True')
insurance_df = pd.read.csv(r'D:/streamlit_env/（医疗费用预测数据）insurance-chinese.csv', encoding='gbk')
output = insurance_df['医疗费用']
features =insurance_df[['年龄','性别','BMI','子女数量','是否吸烟','区域']]
features = pd.get_dummies(features)
x_train, x_test, y_train, y_test = train_test_split(features, output,train_size=0.8)
rfr = RandomForestRegressor()
frf.fit(x_train, y_train)
y_pred = rfr.predict(x_test)
r2 = r2_score(y_test, y_pred)
print(f'改模型的可决系数(R-squared)是：{r2}')
