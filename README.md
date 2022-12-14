<h1>appsolution-task-fast-search-api</h1>

>*Преа́мбула: в связи со спецификой условий выполнения задачи, код далее написан исходя из:*
>   - *Сначала функционал, потом оптимизация.*
>
> *Автор репозитОрия понимaeт, что его код далек от идеала и во многом не соответствет принципу DRY, поэтому будет рад воспринимать любою критику кода.*

<!-- [_TOC_] -->
- [Description](#description)
- [run](#run)
- [usage](#usage)

## Description ##
Необходимо написать очень простой поисковик по текстам документов.
Данные хранятся в БД по желанию, поисковый индекс в эластике.
Ссылка на тестовый массива данных: [[csv](https://api.onedrive.com/v1.0/shares/u!aHR0cHM6Ly8xZHJ2Lm1zL3UvcyFBdldqdXEtLW5zblNrYW8yUzVzMnpUTHpNMHBweHc_ZT1RQnJIMGQ/root/content)
Уже находится в корневой папке проекта, скачивать не обязательно.
#### Структура БД
- `id` - уникальный для каждого документа
- `rubrics` - массив рубрик
- `text` - текст документа
- `created_date` - дата создания документа
#### Структура Индекса
- `id` - id из базы
- `text` - текст из структуры БД
#### Необходимые методы
- сервис должен принимать на вход произвольный текстовый запрос, искать по тексту документа в индексе и возвращать первые 20 документов со всем полями БД, упорядоченные по дате создания
- удалять документ из БД и индекса по полю  `id`
#### Технические требования
- Любой Python фреймворк кроме Django и DRF
- `README` с гайдом по поднятию
- `docs.json` - документация к сервису в формате OpenAPI
#### Программа максимум
- функциональные тесты
- сервис работает в Docker
- асинхронные вызовы
---
# run
1. Скопировать репозиторий
```sh
git clone https://github.com/entropax/appsolution_task_fastapi_search
```
2. Запустить сервис
```sh
docker-compose up -d
```
3. Синхронизировать БД с тестовыи csv
```sh
python3 converter.py
```
4. Перезапустить сервис
```sh
docker-compose stop && docker-compose up -d; docker ps
```

# usage
[All API documentation on :8000 port](http://127.0.0.1:8000/redoc)
1. поиск по тексту -
```
GET http://127.0.0.1:8000/posts/search?text=текст
```
2. удаление по идентификатору
```
DELETE http://127.0.0.1:8000/posts/delete
json in body like: {"id" : 93}
```
