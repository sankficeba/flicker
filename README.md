# Веб-приложение каталога товаров

Веб-приложение с каталогом товаров, контейнеризированное с помощью Docker.

## Запуск с помощью Docker Compose

```bash
docker-compose up --build
```

Приложение будет доступно по адресу: http://localhost:5000

## Запуск с помощью Docker

```bash
# Сборка образа
docker build -t products-app .

# Запуск контейнера
docker run -p 5000:5000 products-app
```

## Структура проекта

- `app.py` - Flask приложение
- `templates/products.html` - HTML шаблон страницы товаров
- `Dockerfile` - конфигурация Docker образа
- `docker-compose.yml` - конфигурация Docker Compose
- `requirements.txt` - зависимости Python

## Остановка

Для остановки контейнера используйте:
```bash
docker-compose down
```

