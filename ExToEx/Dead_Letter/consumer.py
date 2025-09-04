import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch=connection.channel()

#now we need to declare master exchange

ch.exchange_declare(exchange='master', exchange_type='direct')
ch.queue_declare(queue='masterq', arguments={
    'x-dead-letter-exchange':'dlx',
    'x-message-ttl':3000,
    'x-max-length':20
})
ch.queue_bind(queue='masterq',exchange='master', routing_key='home')

#here we declare dead letter exchange

ch.exchange_declare(exchange='dlx', exchange_type='fanout')
ch.queue_declare(queue='dlxq')
ch.queue_bind(queue='dlxq',exchange='dlx')



def dlx_callback(ch, method, properties, body):
    print(f'Dead Letter Message: {body.decode()}')

ch.basic_consume(queue='dlxq',auto_ack=True,on_message_callback=dlx_callback)
print('*** Waiting for messages. To exit press CTRL+C ***')
ch.start_consuming()
