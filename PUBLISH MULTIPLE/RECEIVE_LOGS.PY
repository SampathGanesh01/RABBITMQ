import pika
from pika.spec import Channel
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
Channel = connection.channel()
Channel.exchange_declare(exchange='logs',exchange_type='fanout')
#above we are declaring a exchange 
#we can declare any times it is not a problem 

result = Channel.queue_declare(queue='',exclusive=True)
#here we are not declaring a queue which means it will create 
#a random queue after work it will be deleted automatcally 
queue_name = result.method.queue
Channel.queue_bind(exchange='logs',queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+X')
def callback(ch,method,properties,body):
    print(" [x] %r" % body)
Channel.basic_consume(queue=queue_name,on_message_callback=callback,auto_ack=True)
Channel.start_consuming()