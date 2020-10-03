# API automation tests (Python + Pytest + Allure)

### Реализованы тесты для следующих методов:
+ get-dependent-offers (получение зависимых предложений)
+ get-independent-offers (получение независимых предложений)
+ get-active-banners (получение активный баннеров)
+ get-version (получение информации о текущей версии)
+ register-sale (регистрация продажи лотерейного билета посредством доп. предложения)

### Запуск тестов:

pytest

### Генерация файлов для отчёта allure:

pytest --alluredir allure-results

### Запуска сервера для просмотра отчёта:

allure serve allure-results