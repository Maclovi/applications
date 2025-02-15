## Имплементация чистой архитектуры

<!--toc:start-->

- [Имплементация чистой архитектуры](#имплементация-чистой-архитектуры)
- [Необходимый минимум для запуска проекта](#необходимый-минимум-для-запуска-проекта)
- [Клонирование проекта и настройка окружения](#клонирование-проекта-и-настройка-окружения)
- [Запуск проекта с помощью Docker](#запуск-проекта-с-помощью-docker)
- [Запуск веб-приложения без Docker](#запуск-веб-приложения-без-docker)
- [Мануальное тестирование](#мануальное-тестирование)
- [Запуск тестов](#запуск-тестов)
- [CLI-kafka](#cli-kafka)
- [Автор](#автор)
<!--toc:end-->

Этот проект представляет собой реализацию чистой архитектуры, разработанной Робертом Мартином (дядей Бобом). Он позволяет пользователям отправлять заявки, которые сохраняются в базе данных и публикуются в топик Kafka. Проект полностью покрыт тестами (100%).

[![GitHub License](https://img.shields.io/github/license/Maclovi/pure-architecture-fastapi)](https://github.com/Maclovi/applications/blob/main/LICENSE)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/Maclovi/applications/pr_tests.yaml)](https://github.com/Maclovi/pure-architecture-fastapi/actions)

---

## Необходимый минимум для запуска проекта

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/) и [Docker Compose](https://docs.docker.com/compose/) (последние версии)

## Клонирование проекта и настройка окружения

Следуйте этим шагам для клонирования проекта и активации окружения:

```bash
git clone https://github.com/Maclovi/applications
cd applications
cp .env.dist .env

python -m venv .venv
source .venv/bin/activate
source ./scripts/set_variables.sh

pip install -e ".[dev]"
pre-commit install
```

## Запуск проекта с помощью Docker

Чтобы запустить проект с помощью Docker, выполните следующую команду:

```bash
docker compose up
```

## Запуск веб-приложения без Docker

Если вы хотите запустить веб-приложение без использования Docker, выполните следующие команды:

```bash
docker compose up -d postgres kafka
./scripts/start.sh
```

## Мануальное тестирование

Чтобы протестировать API, перейдите по следующему адресу:

- [Swagger UI](http://localhost:8000/docs)

Или с помощью curl:

```bash
curl -G "http://localhost:8000/applications?page=1&size=25&user_name=Maclovi"

curl -X POST "http://localhost:8000/applications" \
	-H "Content-Type: application/json" \
	-d '{"user_name": "Maclovi", "description": "Some description"}'
```

## Запуск тестов

Для запуска тестов выполните следующую команду:

```bash
docker compose up -d postgres # тесты зависят от postgres
./scripts/test_cov.sh
```

## CLI-kafka

Для проверки топиков, просмотра сообщений и описания, используйте следующие команды:

```bash
./scripts/kafka_cli.sh --list # Показать список топиков
./scripts/kafka_cli.sh --show <topic_name> # Показать сообщения из указанного топика
./scripts/kafka_cli.sh --describe <topic_name> # Показать описание указанного топика
```

## Автор

**Сергей** - [GitHub Профиль](https://github.com/Maclovi)
