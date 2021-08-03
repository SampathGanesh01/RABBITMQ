import pika
from pika import connection
from pika import channel
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='HELLO')
channel.basic_publish(exchange='',routing_key='HELLO',body='HELLO EBIBIL !')
print('MESSAGE PUBLISHED SUCCESFULLY')
connection.close()