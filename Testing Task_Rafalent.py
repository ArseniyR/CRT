'''Тест-кейсы'''

'''#1 Позитивная регистрация пользователя с заполнением всех полей'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# signup_section = driver.find_element(By.CSS_SELECTOR, '[href="/signup"]')
# signup_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('Homer@mail.ru')
# name = driver.find_element(By.CSS_SELECTOR, '[name = "name"]')
# name.send_keys('Homer')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('123456')
# signup_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# signup_button.click()
# time.sleep(3)
# driver.quit()

'''#2 Регистрация пользователя на уже занятый адрес с заполнением всех полей'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# signup_section = driver.find_element(By.CSS_SELECTOR,'[href="/signup"]')
# signup_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('homer@mail.ru')
# name = driver.find_element(By.CSS_SELECTOR, '[name = "name"]')
# name.send_keys('Homer2')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('1234567')
# signup_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# signup_button.click()
# notification = driver.find_element(By.CLASS_NAME, 'notification')
# assert notification.is_displayed()
# time.sleep(3)
# driver.quit()

'''#3 Позитивная регистрация пользователя с заполнением только обязательных полей'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# signup_section = driver.find_element(By.CSS_SELECTOR, '[href="/signup"]')
# signup_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('ggg@mail.ru')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('123456')
# signup_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# signup_button.click()
# time.sleep(3)
# driver.quit()

'''#4 Попытка регистрации с пустыми полями ввода'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# signup_section = driver.find_element(By.CSS_SELECTOR, '[href="/signup"]')
# signup_section.click()
# signup_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# signup_button.click()
# notification = driver.find_element(By.CLASS_NAME, 'notification')
# assert notification.is_displayed()
# time.sleep(3)
# driver.quit()

'''#5 Регистрация пользователя с заполнением только поля Email'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# signup_section = driver.find_element(By.CSS_SELECTOR, '[href="/signup"]')
# signup_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('rte@mail.ru')
# signup_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# signup_button.click()
# notification = driver.find_element(By.CLASS_NAME, 'notification')
# assert notification.is_displayed()
# time.sleep(3)
# driver.quit()

'''#6 Регистрация пользователя с заполнением только поля Password'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# signup_section = driver.find_element(By.CSS_SELECTOR, '[href="/signup"]')
# signup_section.click()
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('123456')
# signup_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# signup_button.click()
# notification = driver.find_element(By.CLASS_NAME, 'notification')
# assert notification.is_displayed()
# time.sleep(3)
# driver.quit()

'''#7 Регистрация пользователя с заполнением только поля Name'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# signup_section = driver.find_element(By.CSS_SELECTOR, '[href="/signup"]')
# signup_section.click()
# name = driver.find_element(By.CSS_SELECTOR, '[name = "name"]')
# name.send_keys('Albert')
# signup_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# signup_button.click()
# notification = driver.find_element(By.CLASS_NAME, 'notification')
# assert notification.is_displayed()
# time.sleep(3)
# driver.quit()

'''#8 Регистрация пользователя с заполнением только полей Email, Name'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# signup_section = driver.find_element(By.CSS_SELECTOR, '[href="/signup"]')
# signup_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('ddd@mail.ru')
# name = driver.find_element(By.CSS_SELECTOR, '[name = "name"]')
# name.send_keys('Albert')
# signup_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# signup_button.click()
# notification = driver.find_element(By.CLASS_NAME, 'notification')
# assert notification.is_displayed()
# time.sleep(3)
# driver.quit()

'''#9 Регистрация пользователя с заполнением только полей Name, Password'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# signup_section = driver.find_element(By.CSS_SELECTOR, '[href="/signup"]')
# signup_section.click()
# name = driver.find_element(By.CSS_SELECTOR, '[name = "name"]')
# name.send_keys('Albert')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('123456')
# signup_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# signup_button.click()
# notification = driver.find_element(By.CLASS_NAME, 'notification')
# assert notification.is_displayed()
# time.sleep(3)
# driver.quit()

'''#10 Регистрация пользователя с заполнением только поля Email уже занятым адресом'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# signup_section = driver.find_element(By.CSS_SELECTOR, '[href="/signup"]')
# signup_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('homer@mail.ru')
# signup_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# signup_button.click()
# notification = driver.find_element(By.CLASS_NAME, 'notification')
# assert notification.is_displayed()
# time.sleep(3)
# driver.quit()

'''#11 Стандартная регистрация пользователя, затем регистрация пользователя под другим email, но под тем же именем'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# signup_section = driver.find_element(By.CSS_SELECTOR, '[href="/signup"]')
# signup_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('ee@mail.ru')
# name = driver.find_element(By.CSS_SELECTOR, '[name = "name"]')
# name.send_keys('Michael')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('123456')
# signup_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# signup_button.click()
# signup_section = driver.find_element(By.CSS_SELECTOR, '[href="/signup"]')
# signup_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('ff@mail.ru')
# name = driver.find_element(By.CSS_SELECTOR, '[name = "name"]')
# name.send_keys('Michael')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('1234567')
# signup_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# signup_button.click()
# time.sleep(3)
# driver.quit()

'''#12 Регистрация пользователя с вводом слова в поле email'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# signup_section = driver.find_element(By.CSS_SELECTOR, '[href="/signup"]')
# signup_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('arny')
# name = driver.find_element(By.CSS_SELECTOR, '[name = "name"]')
# name.send_keys('Arny')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('123456')
# url = driver.current_url
# signup_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# signup_button.click()
# assert url == driver.current_url
# time.sleep(3)
# driver.quit()

'''#13 Регистрация пользователя с вводом слова и знака @ в поле email'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# signup_section = driver.find_element(By.CSS_SELECTOR, '[href="/signup"]')
# signup_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('arny@')
# name = driver.find_element(By.CSS_SELECTOR, '[name = "name"]')
# name.send_keys('Arny')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('123456')
# url = driver.current_url
# signup_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# signup_button.click()
# assert url == driver.current_url
# time.sleep(3)
# driver.quit()

'''#14 Регистрация пользователя с эл.адресом, в котором не дописан домен верхнего уровня (.com)'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# signup_section = driver.find_element(By.CSS_SELECTOR, '[href="/signup"]')
# signup_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('arny@gmail')
# name = driver.find_element(By.CSS_SELECTOR, '[name = "name"]')
# name.send_keys('Arny')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('123456')
# url = driver.current_url
# signup_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# signup_button.click()
# assert url == driver.current_url
# time.sleep(3)
# driver.quit()

'''#15 Регистрация пользователя с эл.адресом, частично написанным кириллицей'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# signup_section = driver.find_element(By.CSS_SELECTOR, '[href="/signup"]')
# signup_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('SchАрни@gmail.com')
# name = driver.find_element(By.CSS_SELECTOR, '[name = "name"]')
# name.send_keys('Arny')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('123456')
# url = driver.current_url
# signup_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# signup_button.click()
# assert url == driver.current_url
# time.sleep(3)
# driver.quit()

'''#16 Регистрация с паролем длиной 4 символа'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# signup_section = driver.find_element(By.CSS_SELECTOR, '[href="/signup"]')
# signup_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('hs@mail.ru')
# name = driver.find_element(By.CSS_SELECTOR, '[name = "name"]')
# name.send_keys('Homer')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('ab12')
# signup_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# signup_button.click()
# time.sleep(3)
# driver.quit()

'''#17 Регистрация с паролем длиной 25 символов'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# signup_section = driver.find_element(By.CSS_SELECTOR, '[href="/signup"]')
# signup_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('hs2@mail.ru')
# name = driver.find_element(By.CSS_SELECTOR, '[name = "name"]')
# name.send_keys('Homer')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('abcdefghijklmno1234567890')
# signup_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# signup_button.click()
# time.sleep(3)
# driver.quit()

'''#18 Регистрация с паролем длиной 25 символов'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# signup_section = driver.find_element(By.CSS_SELECTOR, '[href="/signup"]')
# signup_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('hs3@mail.ru')
# name = driver.find_element(By.CSS_SELECTOR, '[name = "name"]')
# name.send_keys('Homer')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('          ')
# signup_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# signup_button.click()
# time.sleep(3)
# driver.quit()


'''Предусловие перед следующими тест-кейсами'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("http://localhost:5000/")
# signup_section = driver.find_element(By.CSS_SELECTOR, '[href="/signup"]')
# signup_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('marc@gmail.com')
# name = driver.find_element(By.CSS_SELECTOR, '[name = "name"]')
# name.send_keys('Marc')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('marc1234')
# signup_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# signup_button.click()
# driver.quit()

'''#19 Стандартная авторизация пользователя'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# login_section = driver.find_element(By.CSS_SELECTOR, '[href="/login"]')
# login_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('marc@gmail.com')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('marc1234')
# login_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# login_button.click()
# time.sleep(3)
# driver.quit()

'''#20 Авторизация пользователя с активацией чекбокса «Запомнить меня»'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# login_section = driver.find_element(By.CSS_SELECTOR, '[href="/login"]')
# login_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('marc@gmail.com')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('marc1234')
# remember_me_checkbox = driver.find_element(By.CLASS_NAME, 'checkbox')
# remember_me_checkbox.click()
# login_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# login_button.click()
# time.sleep(3)
# driver.quit()

'''#21 Проверка сохранения данных в сессии после авторизации с активацией чекбокса "Запомнить меня" '''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# login_section = driver.find_element(By.CSS_SELECTOR, '[href="/login"]')
# login_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('marc@gmail.com')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('marc1234')
# remember_me_checkbox = driver.find_element(By.CLASS_NAME, 'checkbox')
# remember_me_checkbox.click()
# login_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# login_button.click()
# driver.execute_script("window.open();")
# driver.close()
# driver.switch_to.window(driver.window_handles[0])
# driver.get("http://localhost:5000/")
# profile_section = driver.find_element(By.CSS_SELECTOR, '[href="/profile"]')
# profile_section.click()
# time.sleep(3)
# driver.quit()

'''#22 Проверка прерывания сессии при выходе из личного кабинета вне зависимости от статуса чекбокса "Запомнить меня" '''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# login_section = driver.find_element(By.CSS_SELECTOR, '[href="/login"]')
# login_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('marc@gmail.com')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('marc1234')
# remember_me_checkbox = driver.find_element(By.CLASS_NAME, 'checkbox')
# remember_me_checkbox.click()
# login_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# login_button.click()
# logout_section = driver.find_element(By.CSS_SELECTOR, '[href="/logout"]')
# logout_section.click()
# login_section = driver.find_element(By.CSS_SELECTOR, '[href="/login"]')
# login_section.click()
# time.sleep(3)
# driver.quit()

'''#23 Проверка прерывания сессии при выходе из личного кабинета без выбора чекбокса "Запомнить меня" '''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# login_section = driver.find_element(By.CSS_SELECTOR, '[href="/login"]')
# login_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('marc@gmail.com')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('marc1234')
# login_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# login_button.click()
# logout_section = driver.find_element(By.CSS_SELECTOR, '[href="/logout"]')
# logout_section.click()
# login_section = driver.find_element(By.CSS_SELECTOR, '[href="/login"]')
# login_section.click()
# time.sleep(3)
# driver.quit()

'''#24 Попытка авторизации с пустыми полями ввода '''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# login_section = driver.find_element(By.CSS_SELECTOR, '[href="/login"]')
# login_section.click()
# url = driver.current_url
# login_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# login_button.click()
# assert url == driver.current_url
# time.sleep(3)
# driver.quit()

'''#25 Попытка авторизации с пустым паролем '''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# login_section = driver.find_element(By.CSS_SELECTOR, '[href="/login"]')
# login_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('marc@gmail.com')
# url = driver.current_url
# login_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# login_button.click()
# assert url == driver.current_url
# time.sleep(3)
# driver.quit()

'''#26 Попытка авторизации с пустым email '''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# login_section = driver.find_element(By.CSS_SELECTOR, '[href="/login"]')
# login_section.click()
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('marc1234')
# url = driver.current_url
# login_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# login_button.click()
# assert url == driver.current_url
# time.sleep(3)
# driver.quit()

'''#27 Попытка авторизации с вводом слова вместо email'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# login_section = driver.find_element(By.CSS_SELECTOR, '[href="/login"]')
# login_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('marc')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('marc1234')
# login_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# login_button.click()
# time.sleep(3)
# driver.quit()

'''#28 Попытка авторизации с вводом слова и символа '@' вместо email'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# login_section = driver.find_element(By.CSS_SELECTOR, '[href="/login"]')
# login_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('marc@')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('marc1234')
# login_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# login_button.click()
# time.sleep(3)
# driver.quit()

'''#29 Попытка авторизации с вводом эл.адреса, в котором не дописан домен верхнего уровня (.com) '''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# login_section = driver.find_element(By.CSS_SELECTOR, '[href="/login"]')
# login_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('marc@gmail')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('marc1234')
# login_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# login_button.click()
# time.sleep(3)
# driver.quit()

'''#30 Попытка авторизации с вводом верного эл.адреса и неверного пароля'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# login_section = driver.find_element(By.CSS_SELECTOR, '[href="/login"]')
# login_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('marc@gmail')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('homer1234')
# url = driver.current_url
# login_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# login_button.click()
# assert url == driver.current_url
# time.sleep(3)
# driver.quit()

'''#31 Попытка авторизации с вводом верного эл.адреса и неверного пароля при выбранном чекбоксе «Запомнить меня» '''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# login_section = driver.find_element(By.CSS_SELECTOR, '[href="/login"]')
# login_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('marc@gmail')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('henry1234')
# remember_me_checkbox = driver.find_element(By.CLASS_NAME, 'checkbox')
# remember_me_checkbox.click()
# url = driver.current_url
# login_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# login_button.click()
# assert url == driver.current_url
# time.sleep(3)
# driver.quit()

'''#32 Регистрация и вход пользователя с именем, написанным кириллицей'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# signup_section = driver.find_element(By.CSS_SELECTOR, '[href="/signup"]')
# signup_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('homer01@gmail.com')
# name = driver.find_element(By.CSS_SELECTOR, '[name = "name"]')
# name.send_keys('Гомер')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('123456')
# url = driver.current_url
# signup_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# signup_button.click()
# assert url != driver.current_url
# time.sleep(3)
# login_section = driver.find_element(By.CSS_SELECTOR, '[href="/login"]')
# login_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('homer01@gmail.com')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('123456')
# login_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# login_button.click()
# title = driver.find_element(By.CLASS_NAME, 'title')
# assert title.text == 'Welcome, Гомер!'
# driver.quit()

'''#33 Регистрация и вход с паролем, состоящим из эмодзи'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://localhost:5000/")
# signup_section = driver.find_element(By.CSS_SELECTOR, '[href="/signup"]')
# signup_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('homers@gmail.com')
# name = driver.find_element(By.CSS_SELECTOR, '[name = "name"]')
# name.send_keys('Гомер')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('😂')
# url = driver.current_url
# signup_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# signup_button.click()
# login_section = driver.find_element(By.CSS_SELECTOR, '[href="/login"]')
# login_section.click()
# email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
# email.send_keys('homers@gmail.com')
# password = driver.find_element(By.CSS_SELECTOR, '[name = "password"]')
# password.send_keys('😂')
# login_button = driver.find_element(By.CSS_SELECTOR, '.box .button')
# login_button.click()
# time.sleep(3)
# driver.quit()