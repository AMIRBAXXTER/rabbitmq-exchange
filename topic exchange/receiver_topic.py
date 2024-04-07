import datetime
import sys

from make_connection import make_connection

connection, channel = make_connection('amir', '13761376')

channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

binding_key = sys.argv[1]
result = ''
if not binding_key:
    print('you must send binding key')
    sys.exit(1)
elif binding_key == '*.important':
    result = channel.queue_declare(queue='important')

elif binding_key == '*.unimportant':
    result = channel.queue_declare(queue='unimportant')

channel.queue_bind(exchange='topic_logs',
                   queue=result.method.queue,
                   routing_key=binding_key)
print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    body = body.decode('utf-8')
    if binding_key == '*.important':
        with open('important.txt', 'a') as f:
            f.write(f' [x] {body}, properties: {properties.headers}, {datetime.datetime.now()}\n')
            f.close()
        print('message saved in important.txt')
        ch.basic_ack(delivery_tag=method.delivery_tag)
    
    elif binding_key == '*.unimportant':
        print(f' [x] {body}, routing_key: {method.routing_key}, properties: {properties}')
        ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue=result.method.queue, on_message_callback=callback)

channel.start_consuming()
