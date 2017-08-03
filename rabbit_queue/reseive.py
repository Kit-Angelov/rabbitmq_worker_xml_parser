import pika
from rabbit_queue import config
from worker_parser_xml.loader import main

# соединение с сервером rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(config.host))
channel = connection.channel()

# инициализации очереди для прослушивания (если очередь не создана - создает, если создана - хорошо :) )
channel.queue_declare(config.queue)


# функция обработки сообщения полученного из очереди
def callback(ch, method, properties, body):
    body = body.decode('utf-8')        # тело полученного сообщения ( предполагаем, что это путь до загруженного ZIPа )
    print('body: ', body)
    path_zip, abs_path_zip = str(body).split('|')
    print(path_zip, abs_path_zip)
    main(path_zip, abs_path_zip)       # функция обработки

# базовые настройки прослушки очередь
channel.basic_consume(callback,        # функция - обработчик полученного сообщения
                      queue='test',    # имя очереди для прослушивания
                      no_ack=True)     # дополнительные параметры ( читать документацию )

# старт прослушки очереди
print('start consuming.......')
channel.start_consuming()


