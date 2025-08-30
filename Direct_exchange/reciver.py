import time

import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()
ch.queue_declare(queue='first')

def callback(ch, method, properties, body):
    print(f'this is what we Received : {body}')
    print(method)
    time.sleep(5)
    print('Done !')
    print('____________________________________')
    ch.basic_ack(delivery_tag=method.delivery_tag)
#this function help rabbitmq to send one by one request
ch.basic_qos(prefetch_count=1)
ch.basic_consume(queue='first', on_message_callback=callback)
print('Waiting for message..., if you wanna go out press ctrl+c')
ch.start_consuming()
