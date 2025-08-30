import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
ch =connection.channel()


ch.exchange_declare(exchange='test', exchange_type='topic')
messages={
    'error.logs.important': 'this message is important',
    'info.debug.notimportant': 'this message is not important',
}

for k,v in messages.items():
    ch.basic_publish(exchange='test',
                     routing_key=k,
                     body=v
                     )

print("Sent ...")
connection.close()