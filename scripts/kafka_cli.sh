#!/bin/sh
set -e

# Укажите имя контейнера Kafka
CONTAINER_NAME="kafka"

# Укажите адрес и порт bootstrap-сервера
BOOTSTRAP_SERVER="${KAFKA_HOST}:${KAFKA_PORT}"

case "$1" in
    --list)
        docker exec "$CONTAINER_NAME" kafka-topics.sh --list --bootstrap-server "$BOOTSTRAP_SERVER"
        ;;
    --show)
        if [ -z "$2" ]; then
            echo "Пожалуйста, укажите имя топика для отображения сообщений."
            echo "Использование: $0 --show <topic_name>"
            exit 1
        fi
        docker exec -it "$CONTAINER_NAME" kafka-console-consumer.sh --bootstrap-server "$BOOTSTRAP_SERVER" --topic "$2" --from-beginning
        ;;
    --describe)
        if [ -z "$2" ]; then
            echo "Пожалуйста, укажите имя топика для описания."
            echo "Использование: $0 --describe <topic_name>"
            exit 1
        fi
        docker exec "$CONTAINER_NAME" kafka-topics.sh --describe --topic "$2" --bootstrap-server "$BOOTSTRAP_SERVER"
        ;;
    *)
        echo "Неверная команда."
        echo "Доступные команды:"
        echo "  --list                        Показать список топиков"
        echo "  --show <topic_name>           Показать сообщения из указанного топика"
        echo "  --describe <topic_name>       Показать описание указанного топика"
        exit 1
        ;;
esac
