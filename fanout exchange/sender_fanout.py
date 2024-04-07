import time

from make_connection import make_connection, pika

connection, channel_1 = make_connection('amir', '13761376')

channel_1.basic_qos(prefetch_count=1)

channel_1.exchange_declare(exchange='main', exchange_type='fanout')


channel_1.basic_publish(exchange='main',
                        body='Hello World!',
                        routing_key='',
                        properties=pika.BasicProperties(headers={'user': 'amir', 'age': 25}))

print(" [x] Sent 'Hello World!'")

connection.close()
