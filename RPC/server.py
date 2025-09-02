import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch=connection.channel()

#consuming section for server:

ch.queue_declare(queue='req_queue')
# c_consuming = ch.queue_declare(queue='',exclusive=True)
def callback(ch, method, properties, body):
    print(f'Received request {properties.correlation_id}')
    ch.basic_publish('', routing_key=properties.reply_to, body=f'reply to: {properties.correlation_id}')

ch.basic_consume(queue='req_queue', on_message_callback=callback, auto_ack=True)
print('start consuming')
ch.start_consuming()