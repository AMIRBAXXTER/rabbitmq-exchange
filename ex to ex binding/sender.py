from make_connection import make_connection

connection, channel = make_connection('amir', '13761376')

# create two exchange with different type and bind them together
channel.exchange_declare('first exchange', 'direct')
channel.exchange_declare('second exchange', 'fanout')
channel.exchange_bind('second exchange', 'first exchange')

channel.basic_publish(exchange='first exchange', routing_key='', body='hello world')

print(' [x] Sent "hello world"')
connection.close()
