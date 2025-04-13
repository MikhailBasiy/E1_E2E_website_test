# ⚙️ Структура проекта

## Основные директории
- `tests/` — тесты
- `pages/` — Page Object Model (POM) для разных страниц
- `utils/` — вспомогательные функции
- `conftest.py` — фикстуры pytest
- `README.md` — общая информация
- `requirements.txt` — зависимости

## Page Objects
В `pages/` находятся классы, которые описывают действия на отдельных страницах:
- `main_page.py`
- `catalog_page.py`
- `product_page.py`
- `cart_page.py`
- `checkout_page.py`