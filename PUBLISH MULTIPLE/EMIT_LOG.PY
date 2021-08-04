import pika
import sys

from pika import channel
from pika.spec import Exchange
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs',exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "MESSAGE PUBLISHED BY DECLARING A EXCHANGE"
channel.basic_publish(exchange='logs',routing_key='',body=message)
print(" [x] Sent %r" % message)
connection.close()