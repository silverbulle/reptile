from selenium import webdriver
from bs4 import BeautifulSoup
import selenium
import time
from lxml import etree
import re
import xlrd
import xlwt
import xlutils
from xlutils.copy import copy
import openpyxl as op

page = 1
driver = webdriver.Chrome()

#  http://sjfb.gdstc.gd.gov.cn/sjkf/kjxm?const_dict_id=101003
try:
    driver.get('http://sjfb.gdstc.gd.gov.cn/app/sjkf/kjxm_101003.jsp')
    time.sleep(2)
except selenium.common.exceptions.TimeoutException:
    print("time out of 10 s")
    driver.execute_script('window.stop()')
result = driver.page_source
try1 = re.findall('(?<=<td>).*?(?=</td>)', result)

# for i in try1:
#     print(i, '\n')
cnt = 1
bg = op.load_workbook(r"data.xlsx")
sheet = bg["Sheet1"]
while page < 1584:


    driver.find_element_by_xpath("//a[contains(text(),'下页')]").click()
    time.sleep(3)
    page += 1
    # driver.find_element_by_xpath('//*[@class="paginate_button next"]/href').click()
    # time.sleep(3)
    # selenium的xpath用法，找到包含“下一页”的a标签去点击
    result = driver.page_source

    data = re.findall('(?<=<td>).*?(?=</td>)', result)
    print(data)
    num = 0
    for row in range(cnt, 47506):
        cnt += 1
        for column in range(1, 9):
            sheet.cell(row, column, data[num])
            num += 1
            if num == 239:
                bg.save("data.xlsx")
                break
        if cnt % 30 == 0:
            break
# print(driver.page_source)
# page = BeautifulSoup(driver.page_source, 'html.parser')
# result = etree.HTML(driver.page_source)


# result = etree.tostring(page, encoding='gbk')
# print(result.decode('gbk'))
# result = page.xpath('//div[@class="panel panel-info"]/tbody/')[0]


# print(try1)

# comment = page.find_all(r'listTable_wrapper\S+</div>', class_='a-size-large a-color-base')
# print(page)
driver.close()
driver.quit()
