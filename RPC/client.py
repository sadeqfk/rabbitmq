import uuid
import pika

# in RPC client ,consuming and publishing at the same time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = connection.channel()

# here we build client as consumer :
c_consuming = ch.queue_declare(queue='', exclusive=True)


def on_reply_message(ch, method, properties, body):
    print(f'reply received: {body}')


ch.basic_consume(queue=c_consuming.method.queue,
                 on_message_callback=on_reply_message,
                 auto_ack=True
                 )

# here we build client as publisher :
ch.queue_declare(queue='req_queue')

cor_id = str(uuid.uuid4())
print(f'******this is out cor_id : {cor_id}*******')

ch.basic_publish(exchange='',
                 routing_key='req_queue',
                 body='Hello World!',
                 properties=pika.BasicProperties(
                     correlation_id=cor_id,
                     reply_to=c_consuming.method.queue, ))
print("Request Sent")

ch.start_consuming()
print('waiting for correlations..')