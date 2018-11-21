from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import expected_conditins as EC
from selenium.webdriver.common.by import By
class Qiangpiao(object):

  def __init__(self):
    self.login_url = 'https://kyfw.12306.cn/otn/resources/login.html'
    self.initmy_url = 'https://kyfw.12306.cn/otn/view/index.html'
    self.search_url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'
    self.driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    
  def wait_input(self):
    self.from_station = input('出发点：')
    self.to_station = input('目的点：')
    #yyyy-mm-dd
    self.depart_time = input('出发时间：')
    self.passengers = input('乘客姓名(如有多个乘客，用英文逗号隔开):').split(',')
    self.trains = input('车次(如有多个车次用英文逗号隔开)').split(',')
    
  def _login(self):
    self.driver.get(self.login_url)
    #显式等待
    WebDriverWait(self.driver,1000).until(EC.url_to_be(self.initmy_url))
    print('登陆成功！')
    #隐式等待
    
  def _order_ticket(self):
    #跳转到订票页面
    self.driver.get(self.search_url)
    #等待出发地信息是否输入正确
    WebDriverWait(self.driver,1000).until(EC.text_to_be_present_in_element_value((By.ID,'fromStationText'),self.from_station))
    #等待出发地信息是否输入正确
    WebDriverWait(self.driver,1000).until(EC.text_to_be_present_in_element_value((By.ID,'toStationText'),self.to_station))
    #等待出发地信息是否输入正确
    WebDriverWait(self.driver,1000).until(EC.text_to_be_present_in_element_value((By.ID,'train_date'),self.depart_time))
    #
    WebDriverWait(self.driver,1000).until(EC.text_to_be_clickable((By.ID,'query_ticket')))
    #
    searchBtn = self.driver.find_element_by_id('query_ticket')
    searchBtn.click()
    
  def run(self):
    self._login()
    self._order_ticket()
    
if __name__ == '__main__':
  spider = Qiangpiao()
  spider.run()
