import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    exe_path = "C:\Chrome-driver\chromedriver.exe"  # прописывем путь к драйверу для хрома
    email = '*******@gmail.com'
    password = 'Your_Password'
    # запуск браузера
    browser = webdriver.Chrome(executable_path=exe_path)
    # переходим на страницу логина нашей почты

    browser.get(
        'https://accounts.google.com/v3/signin/identifier?dsh=S-1694431074%3A1683865624021785&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=Af_xneGYhuRG6vvS4sopX_WekR6F13aj3tDJkLERhB42FDYhUWShCz7UCnaTVE72WaxB-33hglNw&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    # таймер, чтобы успел браузер подгрузиться
    time.sleep(1)
    emailElem = browser.find_element(By.XPATH,
                                     '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
    emailElem.send_keys(email)  # вбиваем наш емаил
    emailElem.find_element(By.XPATH,
                           '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()  # находим кнопку next
    time.sleep(5)

    emailElem = browser.find_element(By.XPATH,
                                     '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
    emailElem.send_keys(password)
    emailElem.find_element(By.XPATH,
                           '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
    # emailElem.submit()
    time.sleep(5)

    with open('C:\Chrome-driver\lol.csv', encoding='utf-8') as file:
        email_list = csv.reader(file)
        for row in email_list:
            try:
                browser.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/div').click()

                # нашли кнопку написать
                time.sleep(3)

                browser.find_element(By.XPATH,
                                     '/html/body/div[24]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[1]/td[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/input').send_keys(
                    row[1])
                # нашли строку кому отправить
                # browser.

                time.sleep(1)
                browser.find_element(By.XPATH,
                                     '/html/body/div[24]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[1]/div[2]/div[3]/div/table/tbody/tr/td[2]/div[2]/div').send_keys(
                    'Hello ' + row[2])
                # заполнили тело сообщения

                browser.find_element(By.XPATH,
                                     '/html/body/div[24]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]').click()
                # нажимаем кнопку отправить
                time.sleep(15)

            except Exception:
                print('Error, wait 1 hour')
                time.sleep(3600)

                browser.find_element(By.XPATH,
                                     '/html/body/div[28]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]').click()
                # нажимаем кнопку отправить
                time.sleep(15)

    print("well done")
    # time.sleep(500)
