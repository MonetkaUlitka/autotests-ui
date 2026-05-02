import pytest 

@pytest.fixture 
def clear_books_database() -> None:
    print('[FIXTURE] Удаляем все данные из БД')

@pytest.fixture 
def fill_books_database() -> None:
    print('[FIXTURE] Создаем новые данные в БД')


@pytest.mark.usefixtures('fill_books_database')
def test_read_all_books_in_library():
    print('Reading all books')