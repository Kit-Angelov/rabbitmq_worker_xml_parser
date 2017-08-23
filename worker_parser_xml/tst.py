import pika
import config_queue


class Worker:

    connection = pika.BlockingConnection(pika.ConnectionParameters(config_queue.host))
    channel = connection.channel()
    channel.queue_declare(config_queue.queue, durable=True)

    def __callback(self, ch, method, properties, body):
        pass

    def start(self):
        self.channel.basic_consume(self.__callback, queue='test')

        print('start consuming.......')
        self.channel.start_consuming()




class A:

    def __init__(self):
        self.type = None

    def get_type(self):
        self.type = '1'

    def get_ver(self, type):
        self.type = type
        if self.type in d.keys():
            b_class = d[self.type]
            b = b_class(self.type)
            qq = b.get()
            return qq


class B:

    def __init__(self, type):
        self.type = type

    def get(self):
        return '1232131'

d = {'1': B, '2': B, '3': B}

a = A()
a.get_type()

b = a.get_ver('1')
print(b)
