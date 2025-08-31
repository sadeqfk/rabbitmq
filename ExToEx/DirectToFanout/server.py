import pika

Connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = Connection.channel()

#we need to build destination exchange
ch.exchange_declare(exchange='destination', exchange_type='fanout')

#we need queues
ch.queue_declare(queue='test')

#here we connect them
ch.queue_bind(queue='test', exchange='destination')


def callback(ch, method, properties, body):
    print(f"Received {body}")
    print('----------')
ch.basic_consume(queue='test',
                 auto_ack=True,
                 on_message_callback=callback
                 )
print('Waiting for messages..')
ch.start_consuming()