import os

import boto3

print('hi from py')

queue_name = os.environ.get('QUEUE_NAME')

print(queue_name)

if queue_name is not None:
    sqs = boto3.resource('sqs')
    queue = sqs.Queue(queue_name)
    messages = queue.receive_messages(
        MaxNumberOfMessages=10,
        WaitTimeSeconds=5,
    )
    for message in messages:
        print('message', message)
        print('body', message.body)
