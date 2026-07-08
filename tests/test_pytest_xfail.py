import pytest

@pytest.mark.xfail(reasone= 'Найден баг в приложении, ожидаем ошибку')
def test_with_bug():
    assert 1 == 2




@pytest.mark.xfail(reasone= 'Исправлен баг, но не удалена маркировка')
def test_without_bug2():
    ...