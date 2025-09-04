import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch=connection.channel()

#we just need an excahnge and publish message
ch.exchange_declare(exchange='master', exchange_type='direct')

ch.basic_publish(exchange='master',routing_key='home', body='Hello World')
print("Message Sent..!")
connection.close()