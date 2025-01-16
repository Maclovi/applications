docker exec -it kafka kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic Kafka --from-beginning
docker exec kafka kafka-topics.sh --describe Kafka --bootstrap-server localhost:9092
docker exec kafka kafka-topics.sh --list --bootstrap-server localhost:9092
