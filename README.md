# OOP: Product и Category

Учебный проект: классы `Product` и `Category` для работы с каталогом товаров.

## Что есть

- `catalog.py` — классы `Product`, `Category` и функция `load_catalog_from_json` для загрузки каталога из JSON.
- `test_catalog.py` — тесты (pytest): инициализация `Product` и `Category`, подсчет количества товаров и категорий, загрузка из JSON.
- `products.json` — пример данных каталога.
- `main.py` — демонстрация использования: загружает каталог из `products.json` и выводит его содержимое.

## Классы

`Product(name, description, price, quantity)` — товар.

`Category(name, description, products)` — категория товаров. Атрибуты класса `Category.category_count` и `Category.product_count` автоматически считают общее количество созданных категорий и товаров во всех категориях.

## Установка и запуск

```bash
pip install -r requirements.txt
pytest
python main.py
```
