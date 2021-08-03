'''import pika
import time
from pika.amqp_object import Method
from pika.spec import Channel
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
    host='localost'))
Channel = connection.channel()

Channel.queue_declare(queue='TEST_QUEUE', durable=True)

print('[*] waiting for messages.to exit press CTRL+C')

def callback(ch, method, properties, body):host='localhost'))
channel = connection.channel()
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

Channel.basic_qos(prefetch_count=1)
Channel.basic_consume(queue='TEST_QUEUE',
                    on_message_callback=callback)

Channel.start_consuming()'''

import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='TEST_QUEUE', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='TEST_QUEUE', on_message_callback=callback)

channel.start_consuming()