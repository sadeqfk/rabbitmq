import pika

# credentials = pika.PlainCredentials('fan', '123')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
ch = connection.channel()

ch.exchange_declare(exchange='logs', exchange_type='fanout')
result=ch.queue_declare(queue='', exclusive=True)

ch.queue_bind(queue=result.method.queue, exchange='logs')
print("Waiting for queue")
print(result.method.queue)

def callback(ch, method, properties, body):
    print(f'Recived : {body}')


ch.basic_consume(queue=result.method.queue, on_message_callback=callback, auto_ack=True)
ch.start_consuming()