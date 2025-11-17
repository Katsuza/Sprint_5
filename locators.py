from selenium.webdriver.common.by import By

#Поля и кнопки на странице регистрации
REGISTRATION_NAME_FIELD = (By.XPATH, "//label[text()='Имя']/parent::div/input")  #Поле ввода имени
REGISTRATION_EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/parent::div/input")  #Поле ввода email
REGISTRATION_PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")  #Поле ввода пароля
REGISTRATION_SUMBIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  #Кнопка Зарегестрироваться

INCORRECT_PASSWORD_TEXT = (By.CSS_SELECTOR, "#root > div > main > div > form > fieldset:nth-child(3) > div > p") #Сообщение о некорректном пароле

#Элементы для ввода данных в форме входа
LOGIN_EMAIL_FIELD = (By.XPATH, "//input[@type='text']")
LOGIN_PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")

#Кнопки Войти в аккаунт на разных страницах
MAIN_PAGE_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") #Кнопка Войти в аккаун на гл.странице
FORMS_LOGIN_LINK = (By.CLASS_NAME, 'Auth_link__1fOlj') #Кнопка Войти в форме регистарции/восстановления пароля
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']") #Кнопка Личный Кабинет

REGISTARTION_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']")
PASSWORD_RESET = (By.XPATH, "//a[text()='Восстановить пароль']")


#Главная страница
CONSTRUCTOR_LINK_BUTTON = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p") #Кнопка Конструктор
LOGO_BUTTON = (By.XPATH, "//*[@id='root']/div/header/nav/div/a") #Кнопка-Логотип

LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") #Кнопка "Выход" в Личном кабинете

#Разделы Конструктора
BUNS_BUTTON = (By.XPATH, "//span[text()='Булки']")
SAUCES_BUTTON = (By.XPATH, "//span[text()='Соусы']")
FILLINGS_BUTTON = (By.XPATH, "//span[text()='Начинки']")

BUNS_BUTTON_PARENT = (By.XPATH, "//span[text()='Булки']/..")
SAUCES_BUTTON_PARENT = (By.XPATH, "//span[text()='Соусы']/..")
FILLINGS_BUTTON_PARENT = (By.XPATH, "//span[text()='Начинки']/..")