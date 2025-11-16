# Sprint_5

Проект содержит набор UI-тестов на Selenium и pytest, покрывающих основные пользовательские сценарии сайта Stellar Burgers.

Для запуска:
1. Установить и активировать вирткуальное окружение
2. Установить необходимые зависимости: pip install pytest selenium

Запустить тесты:
pytest -v

Описание тестов:

1. test_constructor_sections – проверяет переходы по секциям в "Конструкторе"

    - test_move_to_fillings_sections_button – переход к секции с начинками по кнопке "Начинки"
    - test_move_to_buns_section_button – переход к секции с булочками по кнопке "Булки"
    - test_move_to_sauces_section_button - переход к секции с соусами по кнопке "Соусы"

2. test_login – проверяет вход по кнопкам "Войти" из разных форм

    - test_login_from_main_page_log_in_to_account_button - вход по кнопке «Войти в аккаунт» на главной
    - test_login_from_personal_account_button - вход через кнопку «Личный кабинет»
    - test_login_from_registration_form_button - вход через кнопку в форме регистрации
    - test_login_from_password_reset_form_button - вход через кнопку в форме восстановления пароля

3. test_personal_account_navigation – проверяет переходы в/из личного кабинета

    - test_transition_to_personal_account_page - переход по клику на «Личный кабинет» из главной страницы
    - test_transaction_to_costructor_page_by_clicking_constructor_button - переход по клику на «Конструктор»
    - test_transaction_to_costructor_page_by_clicking_logo - переход по клику на лого Stellar Burgers
    - test_logout_by_clicking_logout_button - выход из профиля по кнопке «Выйти» в личном кабинете

4. test_registartion – проверяет сценарии с регистрацией

    - test_registation_correct_date_success - успешная регистрация при вводе корректных данных в поля формы
    - test_registartion_short_password_failure - появление ошибка при вводе некорректного пароля
