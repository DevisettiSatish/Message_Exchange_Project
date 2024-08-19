'''
this file is used to send the sender to receiver using the rabbitmq->pika

'''
import pika
connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()

# create exchange
channel.exchange_declare(exchange='meassage',exchange_type='direct')

channel.queue_declare(queue='q4')
channel.queue_bind(queue='q4',exchange='meassage',routing_key='satish')

channel.basic_publish(exchange='meassage',routing_key='satish',body='i am going to hyderabad')

channel.close()