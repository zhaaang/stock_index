import os
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# tmp = pd.read_excel(r"F:\Projects\stock\data\s\1_4.xlsx", dtype='str')
# columns = tmp.loc[:, '证券代码']
# col = ['date', 'b'] + list(columns)
data = pd.DataFrame(data=None)#, columns=col

# r = 0
# l = [tmp['交易日期'][0], 3245] + list(tmp.loc[:, '今收'])
# data.loc[r] = l
# data.loc[1] = l
#
# print(data.head())
# columns = columns.astype('float')
r = -1
for i in range(1, 13):
    for j in range(1, 32):
        if not os.path.exists(r"F:\Projects\stock\data\s\{}_{}.xlsx".format(i, j)) or \
                not os.path.exists(r"F:\Projects\stock\data\b\{}_{}.xlsx".format(i, j)):
            continue
        r += 1
        tmp = pd.read_excel(r"F:\Projects\stock\data\s\{}_{}.xlsx".format(i, j))
        tmp = tmp.set_index(tmp['证券代码'])
        tmp1 = pd.read_excel(r"F:\Projects\stock\data\b\{}_{}.xlsx".format(i, j))
        tmp1 = tmp1.set_index(tmp1['指数简称'])
        data.loc[r, 'date'] = tmp['交易日期'][1]
        data.loc[r, '成份Ｂ指'] = tmp1.loc['成份Ｂ指', '今收']
        data.loc[r, tmp.loc[:, '今收'].index] = tmp.loc[:, '今收']
    print('第{}月读取完成'.format(i))
data1 = data.dropna(axis=1)
data1.to_excel('data.xlsx',index=False)
