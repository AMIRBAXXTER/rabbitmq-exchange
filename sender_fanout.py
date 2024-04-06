import time

import pika

credentials = pika.PlainCredentials('amir', '13761376')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))

channel_1 = connection.channel()

channel_1.basic_qos(prefetch_count=1)

channel_1.exchange_declare(exchange='main', exchange_type='fanout')


channel_1.basic_publish(exchange='main',
                        body='Hello World!',
                        routing_key='',
                        properties=pika.BasicProperties(headers={'user': 'amir', 'age': 25}))

print(" [x] Sent 'Hello World!'")

connection.close()
