from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

#Note, to access XPATH: 
#1. Press Ctrl + Shift + C on your keyboard to open the Developer Tools in your browser.
#2. Move your mouse to the element for which you want the XPath.
#3. Look in the right pane of the Developer Tools to find the XPath of the selected element.

n = int(input("Nhập số lần: "))

# web = webdriver.Firefox() 
web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/e/1FAIpQLSdQ7A33ufRFYnQheD70rsPTwh1P_KOsTXS6Tj-eEnIB4j-O6w/viewform')

time.sleep(1) #give url some time to render


for i in range(n):
    print(f"Number {i + 1}")
    start = time.time()

    submit=web.find_element(By.XPATH,'/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div/div[1]/div/span/span')
    submit.click()
    time.sleep(1.1)

    # Phan 1: Thong tin chung
    # 1. Gioi tinh
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()

    # 2. Bạn đang là sinh viên năm mấy?
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[1]/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()

    # Continue
    submit=web.find_element(By.XPATH,'/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div/div[1]/div[2]/span/span')
    submit.click()
    time.sleep(0.9)

    # Phan 2: Cac yeu to anh huong den ket qua hoc tap theo chuan dau ra cua sinh vien khoi kinh te
    # I: moi truong hoc tap
    # a) 
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()
    # b)
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[4]/span/div[5]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()
    # c)
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[6]/span/div[4]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[6]/span/div[5]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()
    # d)
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[8]/span/div[2]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[8]/span/div[4]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[8]/span/div[5]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()
    # e)
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[10]/span/div[2]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[10]/span/div[3]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[10]/span/div[4]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[10]/span/div[5]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()

    # II: Chat luong giang day
    # a) 
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()
    # b)
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[5]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()
    # c)
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[4]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[5]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()  
    # d)
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[2]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[4]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[5]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()
    # e)
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[2]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[3]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[4]/div/div/div[3]/div', 
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[5]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()

    # III: Gia dinh
    # a)
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()
    # b)
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[4]/span/div[5]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()
    # c)
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[6]/span/div[4]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[6]/span/div[5]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()
    # d)
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[8]/span/div[2]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[8]/span/div[4]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[8]/span/div[5]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()
    # e)
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[10]/span/div[2]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[10]/span/div[3]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[10]/span/div[4]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[10]/span/div[5]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()

    # IV: Moi quan he ban be
    # a)    
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()
    # b)
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[4]/span/div[5]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()
    # c)
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[6]/span/div[4]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[6]/span/div[5]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()
    # d)
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[8]/span/div[2]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[8]/span/div[4]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[8]/span/div[5]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()
    # e)
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[10]/span/div[2]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[10]/span/div[3]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[10]/span/div[4]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[10]/span/div[5]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()

    # V: Phuong phap hoc tap
    # a)
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()
    # b)
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[4]/span/div[5]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()  
    # c)
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[6]/span/div[4]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[6]/span/div[5]/div/div/div[3]/div']    
    option_xpath = random.choice(choices)   
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()
    # d)
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[8]/span/div[2]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[8]/span/div[4]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[8]/span/div[5]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()
    # e)
    choices = ['/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[10]/span/div[2]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[10]/span/div[3]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[10]/span/div[4]/div/div/div[3]/div',
               '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[10]/span/div[5]/div/div/div[3]/div']   
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.1)
    option.click()
    
    # Continue
    submit=web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span')
    submit.click()
    time.sleep(0.9)
    # Loop
    submit=web.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit.click()
    time.sleep(0.9)
    
    print(f'Done with {i + 1}th loop and {time.time()-start}s')
    time.sleep(0.95)

#Note, to access XPATH: 
#1. Press Ctrl + Shift + C on your keyboard to open the Developer Tools in your browser.
#2. Move your mouse to the element for which you want the XPath.
#3. Look in the right pane of the Developer Tools to find the XPath of the selected element.

# web = webdriver.Chrome()
# web.get('google form link here')

# time.sleep(2) #give url some time to render

# #short paragraph 
# Name = 'John' #your input
# name=web.find_element(By.XPATH,'xpath of short paragraph answer here') 
# name.send_keys(Name)

# #multiple choice answer
# category=web.find_element(By.XPATH,'xpath of clickable options')
# time.sleep(2)
# category.click()

# # Time input
# hour_xpath = 'XPath for the hour input' 
# minute_xpath = 'XPath for the minute input'  

# # Find the elements for hour, minute
# hour_field = web.find_element(By.XPATH, hour_xpath)
# minute_field = web.find_element(By.XPATH, minute_xpath)

# # Enter the time values
# hour_field.send_keys('17') #5pm = 17:00
# time.sleep(2)
# minute_field.send_keys('00')
# time.sleep(2)

# submit=web.find_element(By.XPATH,'xpath of submit button')
# submit.click()
