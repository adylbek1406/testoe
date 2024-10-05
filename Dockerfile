# Используем базовый образ Python
FROM python:3.9-slim

# Устанавливаем переменные окружения для управления Python
ENV PYTHON_VERSION=3.9
ENV DJANGO_ENV=production

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt /app/
COPY requirements.in /app/

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    libpq-dev \
    python3-dev \
    build-essential \
    gcc \
    libhdf5-dev  # Для работы с h5py

# Обновляем pip до последней версии
RUN pip install --upgrade pip

# Устанавливаем pip-tools
RUN pip install pip-tools

# Компилируем файл зависимостей
RUN pip-compile requirements.in

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir --no-deps -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . /app/

# Команда для запуска сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]