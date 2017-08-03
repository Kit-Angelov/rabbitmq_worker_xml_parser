import pika


def send(body):
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='test')

    channel.basic_publish(exchange='',
                          routing_key='test',
                          body=body)
