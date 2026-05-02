#example

import pytest

SYSTEM_VERSION = "v1.2.0"  # Для примера укажем версию тестируемой системы

#skipif example
@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.3.0",  # Пропустим автотес, если версия системы равна v1.3.0
    reason="Тест не может быть запущен на версии системы v1.3.0"
)
def test_system_version_valid():  # В текущей конфигурации этот тест запустится
    pass


@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.2.0",  # Пропустим автотес, если версия системы равна v1.2.0
    reason="Тест не может быть запущен на версии системы v1.2.0"
)
def test_system_version_invalid():  # Этот автотест не запустится
    pass


#xfail example
@pytest.mark.xfail(reason="Известная ошибка, исправление в следующем релизе")
def test_known_issue():
    pass

#skip example

@pytest.mark.skip(reason="Фича в разработке")
def test_feature_in_development():
    pass

