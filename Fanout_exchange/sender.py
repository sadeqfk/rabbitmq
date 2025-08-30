import pika


# credentials = pika.PlainCredentials('fan', '123')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', ))
ch =connection.channel()

ch.exchange_declare(exchange='logs', exchange_type='fanout')
ch.basic_publish(exchange='logs',routing_key='', body='Fanout_exchange example')

print('Message Published')
connection.close()
