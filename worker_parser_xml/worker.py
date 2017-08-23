from .mine_load import Loader, Miner
import pika
import config_queue
import random
import os


class Worker:

    def __init__(self, base_dir, queue):
        self.base_dir = base_dir
        self.queue = queue
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(config_queue.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(config_queue.queue, durable=True)
        self.channel.basic_qos(prefetch_count=1)
        self.worker_id = random.randint(1, 100)
        self.base_path = os.path.join(self.base_dir, self.worker_id)  # базовая диретория воркера

    def handler(self, ch, method, properties, body):
        print('Received massage')
        body = body.decode('utf-8')
        print('body: ', body)
        # Обработка данных
        miner = Miner(self.base_path)
        data = miner.get_data(body)
        loader = Loader()
        loader.load(data=data)

        print('Done')
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def start(self):
        os.mkdir(self.base_path)
        self.channel.basic_consume(self.handler, queue=self.queue)
        print('start consuming.......')
        self.channel.start_consuming()




