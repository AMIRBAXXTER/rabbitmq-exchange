import sys
from make_connection import make_connection

connection, channel = make_connection('amir', '13761376')

channel.exchange_declare('alternate-ex', 'fanout')
channel.exchange_declare('main-ex', 'direct', arguments={'alternate-exchange': 'alternate-ex'})
# use -m for set routing key='main or -a for set routing key='alternate'
if len(sys.argv) > 1:
    print(sys.argv)
    if sys.argv[1] == '-m':
        routing_key = 'main'
    elif sys.argv[1] == '-a':
        routing_key = 'somthing'
    else:
        print('use -m or -a')
        sys.exit(1)
else:
    print('use -m or -a')
    sys.exit(1)
channel.basic_publish('main-ex', routing_key, 'Hello World!')

print(' [x] Sent "Hello World!"')

connection.close()
