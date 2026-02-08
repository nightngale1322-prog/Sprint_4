from main import BooksCollector
import pytest

class TestBooksCollector:

    def test_add_new_book_add_one_succsess(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать?')
        assert len(collector.books_genre) == 1 

    def test_set_book_genre_set_horror_succsess(self):
        collector = BooksCollector()
        collector.add_new_book('Колобок')
        collector.set_book_genre('Колобок', 'Ужасы')
        assert collector.get_book_genre ('Колобок') == 'Ужасы'

    @pytest.mark.parametrize ('name, genre', [['Спящая красавица', 'Фантастика'], ['Котенок Гав','Мультфильмы']])
    def test_get_book_genre_return_two_genre_succsess(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre (name, genre)
        assert collector.get_book_genre (name) == genre

    def test_set_book_genre_genre_not_in_list_no_book(self):
        collector = BooksCollector()
        collector.add_new_book('Ворона и сыр')
        collector.set_book_genre('Ворона и сыр','Мистика')
        assert not collector.get_book_genre ('Ворона и сыр') == 'Мистика'

    def test_get_books_with_specific_genre_get_genre_in_list_success(self):
        collector = BooksCollector()
        collector.add_new_book('Мертвые души')
        collector.set_book_genre('Мертвые души', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Мертвые души']

    @pytest.mark.parametrize ('names, genres', [['Превращение','Ужасы'],['Шерлок Холмс', 'Детективы']])
    def test_get_books_for_children_get_three_books_not_in_genre_age_rating_empty_list(self, names,genres):
        collector = BooksCollector()
        collector.add_new_book(names)
        collector.set_book_genre (names, genres)
        assert collector.get_books_for_children() == []

    @pytest.mark.parametrize ('names, genres', [['Тайны третьей планеты','Фантастика'],['Буратино', 'Мультфильмы'], ['Вредные советы','Комедии']])
    def test_get_books_for_children_get_book_in_genre_age_rating_success(self, names, genres):
        collector = BooksCollector()
        collector.add_new_book(names)
        collector.set_book_genre (names, genres)
        assert names in collector.get_books_for_children()


    @pytest.mark.parametrize('names', [['Автостопом по галактике', 'Мухтар', 'Реквием по мечте']])
    def test_add_book_in_favorites_add_three_books_succsess(self, names):
        collector = BooksCollector()
        for name in names:
            collector.add_new_book(name)
            collector.add_book_in_favorites(name)
        assert len(collector.favorites) == len(names)

    @pytest.mark.parametrize('names', [['Гранатовый браслет', 'Чебурашка', 'О дивный новый мир']])
    def test_delete_book_from_favorites_delete_one_succsess(self, names):
        collector = BooksCollector()
        for name in names:
            collector.add_new_book(name)
            collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(names [0])
        assert len(collector.favorites) == (len(names) - 1)

    def test_get_list_of_favorites_books_get_one_succsess(self):
        collector = BooksCollector()
        collector.add_new_book ('Простоквашино')
        collector.add_book_in_favorites ('Простоквашино')
        collector.get_list_of_favorites_books()
        assert 'Простоквашино' in collector.favorites


    
