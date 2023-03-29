import boto3
import json
import os

sqs = boto3.resource('sqs')

# Load the queue name from the config file
with open('config.json') as f:
    config = json.load(f)
queue_name = config['queue_name']

# Create the SQS queue
queue = sqs.create_queue(QueueName=queue_name)

# Define a function to send a message to the queue
def send_message_to_queue(message):
    queue.send_message(MessageBody=message)
    print(f"Sent message '{message}' to queue '{queue_name}'")

# Send a test message to the queue
send_message_to_queue("Hello, world!")
