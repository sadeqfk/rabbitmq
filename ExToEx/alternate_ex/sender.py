import pika

#we use alternate exchange for rejected request or message
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = connection.channel()

#first build Main Exchange
ch.exchange_declare(exchange='main', exchange_type='direct', arguments={'alternate-exchange': 'alt'})
# build alt Exchange
ch.exchange_declare(exchange='alt', exchange_type='fanout')

ch.basic_publish(exchange='main',routing_key='main',body='Hello we are here..!')
print('Message sent')
connection.close()