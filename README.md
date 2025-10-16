# Brand Ratings Analysis

Проект анализирует рейтинги брендов на основе CSV-файлов с данными о товарах и формирует отчёты, например **average-rating**, где выводится средний рейтинг бренда, отсортированный по убыванию.

---

## Функционал

- Чтение одного или нескольких CSV-файлов с товарами.
- Формирование отчёта **average-rating** с выводом таблицы в консоль.
- Параметры:
  - `--files` — пути к CSV-файлам
  - `--report` — название отчёта

---

## Запуск проекта из Git

Если проект клонируется с GitHub, сначала клонируйте репозиторий и создайте виртуальное окружение:

```bash
# Клонируем репозиторий
git clone https://github.com/Rozzenant/average-rating.git
cd average-rating
![Клонирование репозитория](average-rating\images\image.png)

# Создаём и активируем виртуальное окружение
python -m venv venv
![Создание venv](average-rating\images\image2.png)
# Windows
venv\Scripts\activate
![Активация venv](average-rating\images\image3.png)
# Mac/Linux
source venv/bin/activate

# Устанавливаем зависимости
pip install -r requirements.txt
![Установка зависимостей](average-rating\images\image4.png)

# Запуск отчёта
python main.py --files data/file1.csv data/file2.csv --report average-rating
![Запуск отчёта](average-rating\images\image5.png)

# Запуск тестов с покрытием
pytest --cov=reports tests/
![Тесты](average-rating\images\image6.png)

