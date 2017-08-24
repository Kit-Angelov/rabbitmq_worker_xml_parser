from .mine_load import Loader, MinerXML
import pika
from . import config_queue
import random
import os
import shutil


class Worker:

    def __init__(self, base_dir, queue):
        self.base_dir = base_dir
        self.queue = queue
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(config_queue.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(config_queue.queue, durable=True)
        self.channel.basic_qos(prefetch_count=1)
        self.worker_id = random.randint(1, 1000)
        self.worker_dir = os.path.join(self.base_dir, self.worker_id)  # базовая диретория воркера
        self.properties = None

    def __handler(self, ch, method, properties, body):
        self.properties = properties
        print('Received massage')
        body = body.decode('utf-8')
        print('body: ', body)
        # Обработка данных
        miner = MinerXML(self.worker_dir, body)
        data = miner.get_data()
        loader = Loader(data)
        loader.load()
        print('Done')

        ch.basic_ack(delivery_tag=method.delivery_tag)

    def start(self):
        os.mkdir(self.worker_dir)
        print('Create dir {}'.format(self.worker_dir))
        self.channel.basic_consume(self.__handler, queue=self.queue)
        print('start consuming.......')
        self.channel.start_consuming()

    def __del__(self):
        try:
            shutil.rmtree(self.worker_dir)
            print('Delete dir {}'.format(self.worker_dir))
        except Exception as e:
            print(e)



