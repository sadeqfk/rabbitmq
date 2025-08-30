# publisher
import pika

#adding user
credentials = pika.PlainCredentials('sadeqfk', '123')

connection =pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))
ch = connection.channel()
ch.queue_declare(queue='first')
ch.basic_publish(exchange='',routing_key='first', body='Hello this  is my second message')
print(" Message Sent .. !")
connection.close()