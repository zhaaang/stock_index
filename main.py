import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import Lasso,LassoCV
import warnings
warnings.filterwarnings('ignore')

Lambdas = np.logspace(-5, 2, 50)    #10的-5到10的2次方
lasso_cofficients = []
data = pd.read_excel('data.xlsx')
# print(data.columns)
column = data.columns
X = data.loc[:, column[2:]]
def debug1(s:str):
    return s.replace(',', '')
y = data['成份Ｂ指'].apply(debug1)
train_x, train_y = X.iloc[:200, :], y.iloc[:200]
test_x, test_y = X.iloc[200:, :], y.iloc[200:]
# print(train_x)
# print(train_y)
#
for Lambda in Lambdas:
    lasso = Lasso(alpha=Lambda)
    lasso.fit(train_x, train_y)
    lasso_cofficients.append(lasso.coef_)
plt.plot(Lambdas, lasso_cofficients)
# 对x轴作对数变换
plt.xscale('log')
# 设置折线图x轴和y轴标签
plt.xlabel('Lambda')
plt.ylabel('Cofficients')
# 显示图形
plt.show()

print('查看不同lambda对应多少非零参数')
for i, coff in enumerate(lasso_cofficients):
    num = 0
    for coef in coff:
        if coef != 0:
            num += 1
    print('第{}个 {}--{}'.format(i, round(Lambdas[i], 5), num))


# LASSO回归模型的交叉验证
lasso_cv = LassoCV(alphas=Lambdas, cv=10)
lasso_cv.fit(train_x, train_y)
# 输出最佳的lambda值
lasso_best_alpha = lasso_cv.alpha_
print(lasso_best_alpha)

lasso = Lasso(alpha=lasso_best_alpha)
lasso.fit(train_x, train_y)

dic = {'特征': train_x.columns, '系数': lasso.coef_}
df = pd.DataFrame(dic)
df1 = df[df['系数'] != 0]
# print(df1)

ypre = lasso.predict(X)
plt.plot(ypre, label='predict')
plt.plot(list(y.astype('float')), label='actual')
plt.plot([200, 200], [6500, 8500])
plt.legend()
plt.show()

lasso1 = Lasso(alpha=lasso_best_alpha)
lasso1.fit(train_x, train_y)

dic1 = {'特征': train_x.columns, '系数': lasso.coef_}
df2 = pd.DataFrame(dic)
df3 = df[df['系数'] != 0]
# print(df3)

ypre1 = lasso1.predict(X)
plt.plot(ypre1, label='predict')
plt.plot(list(y.astype('float')), label='actual')
plt.plot([200, 200], [6500, 8500])
plt.legend()
plt.show()

plt.plot(ypre, label='predict1')
plt.plot(ypre1, label='predict2')
plt.show()