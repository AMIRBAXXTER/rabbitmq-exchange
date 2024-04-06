import pika
import sys

credentials = pika.PlainCredentials('amir', '13761376')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='headers_exchange', exchange_type='headers')

if len(sys.argv) == 2:
    if sys.argv[1] == '--all':
        result = channel.queue_declare(queue='all')
        bind_args = {'x-match': 'all', 'color': 'blue', 'size': 'big', 'material': 'plastic'}
    elif sys.argv[1] == '--any':
        result = channel.queue_declare(queue='any')
        bind_args = {'x-match': 'any', 'size': 'big'}

    else:
        print('use --all or --any')
        sys.exit(1)
else:
    print('use --all or --any')
    sys.exit(1)

channel.queue_bind(exchange='headers_exchange', queue=result.method.queue, arguments=bind_args)

print(f' [*] Waiting for messages [{result.method.queue}], [{bind_args}]. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(f'{body}, {properties}')
    print(bind_args)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue=result.method.queue, on_message_callback=callback)

channel.start_consuming()

