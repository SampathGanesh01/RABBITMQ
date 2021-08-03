import pika
import sys
from pika import connection
from pika import channel
from pika.spec import BasicProperties
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='TEST_QUEUE',durable=True)
message = ' '.join(sys.argv[1:])
channel.basic_publish(exchange='',routing_key='TEST_QUEUE',body=message,
                        properties=pika.BasicProperties(delivery_mode=2))
print(" [x] Sent %r" % message)
connection.close()