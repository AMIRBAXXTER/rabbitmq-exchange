from random import randint
from time import sleep

from make_connection import make_connection

connection, channel = make_connection('amir', '13761376')

channel.exchange_declare(exchange='main', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='main', queue=queue_name)


def callback(ch, method, properties, body):
    sleep(randint(0, 3))
    print(f' [x] Received {body}')
    print(properties.headers['user'])
    print(properties.headers['age'])
    print(method)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue=queue_name, on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()
