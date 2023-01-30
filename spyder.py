import time
import os
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')

for i in range(0, 2):
    if i == 0:
        des_file = r"F:\Projects\stock\data\b"
        des = '指数行情.xlsx'
        print('index')
    else:
        des_file = r"F:\Projects\stock\data\s"
        des = '股票行情.xlsx'
        print('stocks')
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "download.default_directory": des_file
    })
    for m in range(1, 13):
        driver = webdriver.Chrome(options=options)
        for d in range(1, 32):
            if i == 0:
                url = "http://www.szse.cn/api/report/ShowReport?SHOWTYPE=xlsx&CATALOGID=1826&TABKEY=tab1&txtBegin" \
                      "Date=2022-{}-{}&txtEndDate=2022-{}-{}&random=0.5599584323982516".format(m, d, m, d)
            else:
                url = "http://www.szse.cn/api/report/ShowReport?SHOWTYPE=xlsx&CATALOGID=1815_stock&TABKEY=tab1&t" \
                      "xtBeginDate=2022-{}-{}&txtEndDate=2022-{}-{}&radioClass=00%2C20%2C30%2CC6%2CC7%2CGE%2" \
                      "C14&txtSite=all&random=0.2280062255314128".format(m, d, m, d)
            driver.get(url)
            time.sleep(2)
            try:
                tmp = pd.read_excel(os.path.join(des_file, des))
            except FileNotFoundError:
                print('!!!!又出现问题了!!!!!')
                print('但是被我解决了')
                continue
            # print(url)
            if tmp.shape[0] == 0:
                os.remove(os.path.join(des_file, des))
                print('{}/{}:remove'.format(m, d))
            else:
                os.rename(os.path.join(des_file, des),os.path.join(des_file, "{}_{}.xlsx".format(m, d)))
                print('{}/{}:save'.format(m, d))
        driver.quit()
