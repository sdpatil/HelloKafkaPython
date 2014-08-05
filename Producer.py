__author__ = 'user'

from kafka.client import KafkaClient
from kafka.producer import SimpleProducer
from datetime import datetime

kafka =  KafkaClient("localhost:9092")

producer = SimpleProducer(kafka)

producer.send_messages("pythontest", "This is message sent from python client " + str(datetime.now().time()) )