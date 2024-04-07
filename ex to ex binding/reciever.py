from make_connection import make_connection

connection, channel = make_connection('amir', '13761376')

channel.exchange_declare('second exchange', 'fanout')
channel.queue_declare('server queue', exclusive=True)
channel.queue_bind('server queue', 'second exchange')


def callback(ch, method, properties, body):
    print(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume('server queue', on_message_callback=callback)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
