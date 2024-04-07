from random import randint
from time import sleep

from make_connection import make_connection

connection, channel = make_connection('amir', '13761376')

def callback(ch, method, properties, body):
    sleep(randint(0, 3))
    print(f' [x] Received {body}')
    print(properties.headers['user'])
    print(properties.headers['age'])
    print(method)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue='direct_queue', on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()
