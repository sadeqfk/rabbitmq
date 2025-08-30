import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
ch=connection.channel()

ch.exchange_declare(exchange='test',exchange_type='topic')
result=ch.queue_declare(queue='', exclusive=True)
ch.queue_bind(queue=result.method.queue,exchange='test',routing_key='#.important')

print('Waiting for messages...')

def callback(ch, method, properties, body):
    with open('error_logs.log', 'a') as log:
        log.write(f'{str(body)}\n')

ch.basic_consume(queue=result.method.queue,on_message_callback=callback, auto_ack=True)
ch.start_consuming()