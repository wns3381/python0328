# web5.py

from selenium import webdriver

driver = webdriver.Chrome('c:\\work\\chromedriver')
driver.implicitly_wait(3)
driver.get('https://google.com')
# driver.get('https://nid.naver.com/nidlogin.login')
# driver.find_element_by_name('id').send_keys('naver_id')
# driver.find_element_by_name('id').send_keys('naver_id')
# driver.find_element_by_name('id').send_keys('my id')
# driver.find_element_by_name('pw').send_keys('my pwd')
# driver.get('https://order.pay.naver.com/home')
# html = driver.page_source
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'html.parser')
# notices = soup.select('div.p_inr > div.p_info > a > span')

# for n in notices:
#     print(n.text.strip())
    