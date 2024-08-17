'''
this file is used to send the message to exchange and queues using Rabbitmq library> pika
'''

import pika
connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()

channel.exchange_declare(exchange='FSDA',exchange_type='direct')

# create queue or queues
channel.queue_declare(queue='q1')
channel.queue_declare(queue='q2')
channel.queue_declare(queue='q3')

# bind

channel.queue_bind(queue='q1',exchange='FSDA',routing_key='sai')
channel.queue_bind(queue='q2',exchange='FSDA',routing_key='kiran')
channel.queue_bind(queue='q3',exchange='FSDA',routing_key='laxmi')

channel.basic_publish(exchange='FSDA',routing_key='kiran',body='i will uploading into the you tube channel')

channel.close()