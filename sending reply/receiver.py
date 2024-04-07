from make_connection import make_connection

connection, channel = make_connection('amir', '13761376')

channel.queue_declare(queue='request_queue')


def callback(ch, method, properties, body):
    print(f'[x] Received: {properties.correlation_id}')
    ch.basic_publish(exchange='', routing_key=properties.reply_to, body=f'send reply to {properties.correlation_id}')
    channel.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue='request_queue', on_message_callback=callback)

print('" [x] client starting"')
channel.start_consuming()
