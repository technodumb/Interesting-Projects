import keyboard
import time
from selenium import webdriver

the_super_secret_codeword = 'YmixP fKfSX'

driver = webdriver.Chrome('Whatsapp_tagger\\chromedriver.exe')
driver.get('https://web.whatsapp.com/')

input("Scan the QR code and press enter.")
input("\n Select the group you want to botify")
names = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/header/div[2]/div[2]/span').get_attribute('title')
# names = names.get_attribute('innerHTML')
names = names.split(', ')
driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]').click()
keyboard.write(f"@{names[0]}")
keyboard.send('Enter')
count = 0
for i in range(1, len(names)):
    if names[i] == 'You':
        continue
    keyboard.write(f"@{names[i]}")
    if names[i] == names[i-1]:
        count+=1
        for j in range(count):
            keyboard.send('Down')
    else:
        count = 0
    keyboard.send('Enter')
