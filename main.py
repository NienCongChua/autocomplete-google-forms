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

web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/e/1FAIpQLSeXPR2ZW7O9nxONcfn3HRFyN0Sb8WazUYWQY8PUNMLfC90ibg/viewform')

time.sleep(1) #give url some time to render

for i in range(5):
    print(f"Number {i + 1}")
    start = time.time()
    # Select one option from multiple choice answers
    choices = ['//*[@id="i6"]/div[3]/div', '//*[@id="i9"]/div[3]/div']
    option_xpath = random.choice(choices)
    # option_xpath = '//*[@id="i6"]/div[3]/div'
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()

    # 2. Bạn đang là sinh viên năm mấy?
    choices = ['//*[@id="i20"]/div[3]/div', '//*[@id="i23"]/div[3]/div', '//*[@id="i26"]/div[3]/div', '//*[@id="i29"]/div[3]/div', '//*[@id="i32"]/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()

    # 3. Bạn đã từng tham gia các khóa học hoặc cuộc thi liên quan đến khởi nghiệp chưa?
    choices = ['//*[@id="i40"]/div[3]/div', '//*[@id="i43"]/div[3]/div', '//*[@id="i46"]/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()

    # 4. Gia đình hoặc bạn bè bạn có ai từng khởi nghiệp không?
    choices = ['//*[@id="i54"]/div[3]/div', '//*[@id="i57"]/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()

    # 5. Bạn có kinh nghiệm làm việc trước đây không?
    choices = ['//*[@id="i65"]/div[3]/div', '//*[@id="i68"]/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()

    # 6. Bạn có dự định khởi nghiệp trong tương lai không?
    choices = ['//*[@id="i76"]/div[3]/div', '//*[@id="i79"]/div[3]/div', '//*[@id="i82"]/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()

    submit=web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span')
    submit.click()
    time.sleep(0.5)

    # 7.  Dưới đây là một  số nhận định về "Ý định khởi nghiệp của sinh viên khoa Quản trị kinh doanh - APD". Bạn hãy thể hiện quan điểm của mình bằng cách đánh dấu vào ô thích hợp.
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[4]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[4]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[6]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[6]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[6]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[8]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[8]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[8]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[8]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[10]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[10]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[10]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[10]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[10]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()


    # 8. Dưới đây là một số nhận định về các yếu tố "Cá nhân" ảnh hưởng đến ý định khởi nghiệp. Bạn hãy thể hiện quan điểm của mình bằng cách đánh dấu vào ô thích hợp.
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[12]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[12]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[12]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[12]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[12]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()

    # 9. Dưới đây là một số nhận định về các yếu tố "Môi trường giáo dục đại học" ảnh hưởng đến ý định khởi nghiệp. Bạn hãy thể hiện quan điểm của mình bằng cách đánh dấu vào ô thích hợp.
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[2]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[4]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[4]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[6]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[6]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[6]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[8]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[8]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[8]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[8]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()

    # 10. Dưới đây là một nhận định về các yếu tố “ Gia đình và bạn bè" ảnh hưởng đến ý định khởi nghiệp. Bạn hãy thể hiện quan điểm của mình bằng cách đánh dấu vào ô thích hợp.
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[4]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[4]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[6]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[6]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[6]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[8]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[8]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[8]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[8]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()

    # 11. Dưới đây là một số nhận định về các yếu tố "Nguồn vốn"  ảnh hưởng đến ý định khởi nghiệp. Bạn hãy thể hiện quan điểm của mình bằng cách đánh dấu vào ô thích hợp.
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[2]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[4]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[4]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[6]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[6]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[6]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[8]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[8]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[8]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[8]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()

    # 12.  Dưới đây là một số nhận định về các yếu tố "Cơ hội và trải nghiệm"  ảnh hưởng đến ý định khởi nghiệp. Bạn hãy thể hiện quan điểm của mình bằng cách đánh dấu vào ô thích hợp.
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[2]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[4]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[4]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[6]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[6]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[6]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()
    choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[8]/span/div[2]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div', 
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[8]/span/div[4]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[8]/span/div[5]/div/div/div[3]/div',
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[8]/span/div[6]/div/div/div[3]/div']
    option_xpath = random.choice(choices)
    option = web.find_element(By.XPATH, option_xpath)
    time.sleep(0.01)
    option.click()

    submit=web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span')
    submit.click()
    time.sleep(0.55)

    submit=web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span')
    submit.click()
    time.sleep(0.55)

    submit=web.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit.click()
    print(f'Done with {i}th loop and {time.time()-start}s')
    time.sleep(0.55)

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
