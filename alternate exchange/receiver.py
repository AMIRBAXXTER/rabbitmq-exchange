from make_connection import make_connection

connection, channel = make_connection('amir', '13761376')

channel.exchange_declare('main-exchange', 'direct', arguments={'alternate-exchange': 'main-exchange'})
channel.exchange_declare('alternate-exchange', 'fanout')

channel.queue_declare(queue='main-queue')
channel.queue_bind('main-queue', 'main-ex', 'main')

channel.queue_declare(queue='alternate-queue')
channel.queue_bind('alternate-queue', 'alternate-ex')


def main_callback(ch, method, properties, body):
    print('from main exchange:', body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def alternate_callback(ch, method, properties, body):
    print('from alternate exchange:', body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue='main-queue', on_message_callback=main_callback)
channel.basic_consume(queue='alternate-queue', on_message_callback=alternate_callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
