import pika

Connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch=Connection.channel()

#here we build our exchanges
ch.exchange_declare(exchange='source', exchange_type='direct')
ch.exchange_declare(exchange='destination', exchange_type='fanout')

#Now we need to binding them
ch.exchange_bind('destination', 'source')

ch.basic_publish(exchange='source', routing_key='', body='Hello World')
print('Message published...')
Connection.close()