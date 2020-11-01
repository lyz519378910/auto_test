from selenium import webdriver
import time
import re

#对象
driver = webdriver.Chrome('C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
#对象打开浏览器
# driver.get('https://www.baidu.com')
#窗体最大化
driver.maximize_window()
driver.set_window_position(200,100)
#设置窗体大小
driver.set_window_size(1280,720)


#1、id定位
# driver.find_element_by_id('kw').send_keys('小新')

#2、name定位
# driver.find_element_by_name('wd').send_keys('懂球帝')

#3、classname定位
# driver.find_element_by_class_name('title-content-title').click()

#4、link_text(超链接)定位
# driver.find_element_by_link_text('新闻').click()

# #5、部分超链接
# driver.find_element_by_partial_link_text('新').click()

# #6、F12 选中目标，再右键Copy xpath(注意s)
# driver.find_element_by_xpath('//*[@id="s-top-left"]/a[1]').click()

# try:
#     #1、法一
#     # for i in range(1,7):
#     #     ele = driver.\
#     #         find_element_by_xpath('//*[@id="s-top-left"]/a['+ str(i) +']')
#     #     print(ele.text)
#
#     #2、法二
#     # ele = driver.find_elements_by_xpath('//*[@id="s-top-left"]/a')
#     # print(len(ele))
#     # for eleme in ele:
#     #     print(eleme.text)
# finally:
#     driver.quit()
# driver.close() #关闭当前窗体
# driver.quit()  #关闭浏览器

# #7、css_selector
# driver.find_element_by_css_selector('#kw').send_keys('xiao xin')

# #8、tag_name
# tag = driver.find_elements_by_tag_name('input')
# print(len(tag))




#点击，进入新闻界面
# driver.find_element_by_xpath('//*[@id="s-top-left"]/a[1]').click()

# ele_sear = driver.find_element_by_xpath('//*[@id="kw"]') #找到输入框
# ele_sear.send_keys('sa')                                 #输入sa
# driver.find_element_by_xpath('//*[@id="su"]').click()    #点击搜索
# time.sleep(2)
# driver.back()     #返回
# time.sleep(2)
# driver.forward()  #前进

driver.get('file:///C:/Users/LYZ/AppData/Local/Temp/Rar$EXa9052.3059/7%E6%9C%8820%E5%8F%B7/jd_reg/jd_reg/demo.html##')
rese = driver.find_element_by_id('userName')
rese.send_keys('write')
gar = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/i').value_of_css_property('background')
# print(gar)
print(re.search('error.png',gar).group())
# print(rese.get_attribute('placeholder'))
























