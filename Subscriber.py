import pika
connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()

def callback(ch,method,properties,body):
    print(body)

channel.basic_consume(queue='q2',on_message_callback=callback,auto_ack=True)
channel.stop_consuming()