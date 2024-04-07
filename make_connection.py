import pika


def make_connection(username, password):
    credentials = pika.PlainCredentials(username, password)

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))

    channel = connection.channel()

    return connection, channel
