__author__ = 'user'

from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer

kafka = KafkaClient("localhost:9092")

print("After connecting to kafka")

consumer = SimpleConsumer(kafka, "my-group", "test")

for message in consumer:
    print(message)

