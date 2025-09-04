import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch=connection.channel()
#build main exchange with queue and bind
ch.exchange_declare(exchange='main', exchange_type='direct', arguments={'alternate-exchange': 'alt'})
ch.queue_declare(queue='mainq')
ch.queue_bind(queue='mainq', exchange='main', routing_key='main')


#build alt exchange with queue and bind
ch.exchange_declare(exchange='alt', exchange_type='fanout')
ch.queue_declare(queue='altq')
ch.queue_bind(queue='altq', exchange='alt')


def alt_callback(ch, method, properties, body):
    print(f'****Message token form alt:{body}****')

def main_callback(ch, method, properties, body):
    print(f'****Message token form main:{body}****')

ch.basic_consume(queue='altq', auto_ack=True, on_message_callback=alt_callback)
ch.basic_consume(queue='mainq', auto_ack=True, on_message_callback=main_callback)

print('waiting for messages')
ch.start_consuming()