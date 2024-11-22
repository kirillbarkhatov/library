import json
from unittest.mock import mock_open, patch

from src.json_worker import JSONWorker


def test_save_to_file(library_data):
    """Тестирование метода save_to_file с использованием mock."""
    # Мокаем open и json.dump, чтобы проверить их взаимодействие
    mock_file = mock_open()

    with patch("builtins.open", mock_file), patch("json.dump") as mock_json_dump:
        json_worker = JSONWorker(file_name="test_library.json")
        json_worker.save_to_file(library_data)

    # Проверяем, что open был вызван с нужными параметрами
    mock_file.assert_called_once_with("data/test_library.json", "w", encoding="UTF-8")

    # Проверяем, что json.dump был вызван с нужными аргументами
    mock_json_dump.assert_called_once_with(library_data, mock_file(), indent=4, ensure_ascii=False)


def test_get_from_file(library_data):
    """Тестирование метода get_from_file с использованием mock."""
    # Мокаем open, чтобы вернуть данные при чтении
    mock_file = mock_open(read_data=json.dumps(library_data))

    with patch("builtins.open", mock_file):
        json_worker = JSONWorker(file_name="test_library.json")
        result = json_worker.get_from_file()

    # Проверяем, что данные, полученные из файла, совпадают с ожидаемыми
    assert result == library_data

    # Проверяем, что open был вызван с нужными параметрами
    mock_file.assert_called_once_with("data/test_library.json", "r", encoding="UTF-8")


def test_delete_from_file(library_data):
    """Тестирование метода delete_from_file с использованием mock."""
    # Мокаем open
    mock_file = mock_open()

    with patch("builtins.open", mock_file), patch("json.dump") as mock_json_dump:
        json_worker = JSONWorker(file_name="test_library.json")
        json_worker.save_to_file(library_data)  # Сначала сохраняем данные
        json_worker.delete_from_file()  # Затем удаляем (должен быть вызван save_to_file с пустым списком)

    # Проверяем, что open был вызван дважды
    assert mock_file.call_count == 2  # Первый раз для save_to_file, второй раз для delete_from_file

    # Проверяем, что json.dump был вызван с пустым списком
    mock_json_dump.assert_called_with([], mock_file(), indent=4, ensure_ascii=False)


def test_check_and_get_file_name():
    """Тестирование статического метода __check_and_get_file_name с использованием mock."""
    # Пример вызова без расширения .json
    file_name = JSONWorker._JSONWorker__check_and_get_file_name("library")
    assert file_name == "library.json"

    # Пример вызова с расширением .json
    file_name = JSONWorker._JSONWorker__check_and_get_file_name("library.json")
    assert file_name == "library.json"
