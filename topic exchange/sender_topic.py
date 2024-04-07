import sys

from make_connection import make_connection, pika

connection, channel = make_connection('amir', '13761376')

channel.queue_declare(queue='important_queue')
channel.queue_declare(queue='unimportant_queue')
channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

# use -i  as first argument for set routing key to message.important
# use -u  as first argument for set routing key to message.unimportant

routing_key = 'message.important' if sys.argv[1] == '-i' else 'message.unimportant' if sys.argv[1] == '-u' else None
if not routing_key:
    raise ValueError('You need to specify a routing key -i or -u')
message = (str(sys.argv[2])) if len(sys.argv) > 2 else 'empty message'

channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message,
                      properties=pika.BasicProperties(headers={'user': 'amir', 'age': 25}))
print(f'message {message} sent to exchange topic_logs with routing key {routing_key}')
connection.close()
