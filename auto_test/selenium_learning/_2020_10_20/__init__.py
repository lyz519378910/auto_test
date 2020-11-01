import time

from pykeyboard import PyKeyboard
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
# driver.get('C:\\Users\\LYZ\\Desktop\\国信安—软件日记\\2刘烨钊—白盒测试、自动化测试、性能测试、'
#                           '安全测试\\测试有关文件\\案例\\自动化\\example.html')
driver.set_window_position(200, 100)
driver.set_window_size(1280, 720)

#一、下拉菜单
#------------------------------------------------------------------
#定位元素
# element = driver.find_element_by_id('Selector')
#实例化select
# select_element = Select(element)            #选择方式选择
#1、文本选择值
# select_element.select_by_visible_text('香蕉')
#2、下表选择
# select_element.select_by_index(2)
#3、值选择
# select_element.select_by_value('orange')
#------------------------------------------------------------------


#二、对话框
#------------------------------------------------------------------
# #定位元素
# element = driver.find_element_by_name('alterbutton')
# #点击
# element.click()
# #实例化
# alert = Alert(driver)
# #获取文本
# print(alert.text)
#------------------------------------------------------------------


#三、页面向下滑
#------------------------------------------------------------------
# driver.execute_script('window.scrollTo(1,400)')
#------------------------------------------------------------------


#四、
#------------------------------------------------------------------
# driver.find_element_by_name('promptbutton').click()
# alert = Alert(driver)
# #alert输入
# alert.send_keys('123123')
# #alert确认
# alert.accept()
# #alert取消
# alert.dismiss()
# time.sleep(5)
# driver.quit()
#------------------------------------------------------------------


#五、上传图片
#------------------------------------------------------------------
# upload = driver.find_element_by_name('attach[]')
# upload.send_keys('D:\\图片\\1.PNG')
#------------------------------------------------------------------


#隐式等待
# driver.get('https://www.12306.cn/')
# driver.implicitly_wait(30)
# try:
#     driver.find_element_by_xpath('//*[@id="s-top-left"]/a')
#     wait = WebDriverWait(driver,5)
#     wait.until(expected_conditions.presence_of_element_located)
#     driver.find_element_by_id('sw').send_keys('12321')
# except Exception as e:
#     driver.quit()
#     e.with_traceback()


#六、鼠标、键盘
#------------------------------------------------------------------
# from selenium.webdriver import ActionChains   导包

driver.get('https://www.baidu.com')
#实例化
actions = ActionChains(driver)
# element = driver.find_element_by_link_text('新闻')
# #点击
# actions.click(element).perform()    #perform()  执行的意思

# new_element = driver.find_element_by_id('kw')
# #输入
# new_element.send_keys('12321')
# #双击
# actions.double_click(new_element).perform()

#移动
# element = driver.find_element_by_link_text('新闻')
# actions.move_to_element(element).perform()
# actions.click().perform()


#拖拽
# driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# driver.switch_to.frame('iframeResult')             #切frame
# source = driver.find_element_by_id('draggable')
# target = driver.find_element_by_id('droppable')
# actions.drag_and_drop(source,target).perform()


#右键
element = driver.find_element_by_link_text('新闻')
actions.context_click(element).perform()
pk = PyKeyboard()
pk.press_key()
# pk.press_key()


#------------------------------------------------------------------

#------------------------------------------------------------------





# driver.execute_script('window.scrollTo(1,1000)')
# s_e = driver.find_element_by_id('jumpMenu')
# selc = Select(s_e)
# selc.select_by_visible_text('百度一下，你就知道')
# # print(driver.title)             #检查title
# # print(driver.page_source)       #检查页面
# for v in driver.window_handles:
#     driver.switch_to.window(v)
#     if driver.title == '百度一下，你就知道':
#         break

# find_window(name)                     #定义一个方法
# for v in driver.window_handles:
#     driver.switch_to.window(v)
#     if driver.title == name:
#         break

# driver.find_element_by_id('kw').send_keys('12306')
# driver.find_element_by_id('su').click()



# driver.get('https://www.12306.cn/')
# ele = driver.find_element_by_id('fromStationText')
# ele.click()
# ele.send_keys('成都')
# ele.send_keys(Keys.ENTER)
#
# ele1 = driver.find_element_by_id('toStationText')
# ele1.click()
# ele1.send_keys('北京')
# ele1.send_keys(Keys.ENTER)
#
# driver.execute_script("document.getElementById('train_date').readOnly=false")
# # d = driver.find_element_by_id('train_date')
# # d.click()
# # d.clear()
# # time.sleep(5)
# # d.send_keys('2020-10-25')
# # d.send_keys(Keys.ENTER)
# driver.execute_script("document.getElementById('train_date').value = '2020-10-22'")

#点击被遮挡的按钮
# web_element = driver.find_element_by_id( 'search_one' )
# driver.execute_script('arguments[0].click()',web_element)

# driver.find_element_by_xpath('/html/body/div[10]/div[1]/div[2]/div[25]/div').click()

























