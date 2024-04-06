import pika
import sys

credentials = pika .PlainCredentials('amir', '13761376')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='headers_exchange', exchange_type='headers')
if len(sys.argv) == 2:
    if sys.argv[1] == '--all':
        properties = pika.BasicProperties(headers={'color': 'blue', 'size': 'big'})

    elif sys.argv[1] == '--any':
        properties = pika.BasicProperties(headers={'color': 'blue'})

    else:
        print('use --all or --any')
        sys.exit(1)
else:
    print('use --all or --any')
    sys.exit(1)

channel.basic_publish(routing_key='', exchange='headers_exchange', body='Hello World!', properties=properties)

print(f'[x] Sent {sys.argv[1]} message')
connection.close()

