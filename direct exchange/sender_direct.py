from make_connection import make_connection
import pika

connection, channel = make_connection('amir', '13761376')

channel.queue_declare(queue='direct_queue')

channel.basic_qos(prefetch_count=1)

channel.basic_publish(exchange='',
                      routing_key='direct_queue',
                      body='Hello World!',
                      properties=pika.BasicProperties(headers={'user': 'amir', 'age': 25}))

print(" [x] Sent 'Hello World!'")

connection.close()

