import pytest


@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] отправляем данные в сервис аналитики")


@pytest.fixture(scope='session')
def settings():
    print("[SESSION] Инициализируем настройки")

@pytest.fixture(scope='class')
def user():
    print("[CLASS] Создаем данные пользователя")

@pytest.fixture(scope='function')
def browser():
    print("[FUNCTION] Открываем браузер на каждый вызов функции")



class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        ...


    def test_user_can_create_course(self, settings, user, browser):
        ...

class TestActionFlow:
    def test_user_account(self, settings, user, browser):
        ...