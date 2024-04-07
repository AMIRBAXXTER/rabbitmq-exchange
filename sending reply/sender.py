from uuid import uuid4

from make_connection import make_connection, pika

connection, channel = make_connection('amir', '13761376')

reply_queue = channel.queue_declare('', exclusive=True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue=reply_queue.method.queue, on_message_callback=callback)

channel.queue_declare(queue='request_queue')

correlation_id = str(uuid4())
print(f'sending request: {correlation_id}')

channel.basic_publish('', routing_key='request_queue', body='sending request for reply',
                      properties=pika.BasicProperties(
                          reply_to=reply_queue.method.queue,
                          correlation_id=correlation_id,
                      ))

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()
