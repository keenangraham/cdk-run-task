import os

import boto3

import time

print('hi from py')

queue_name = os.environ.get('QUEUE_NAME')

print(queue_name)

handled = 0

if queue_name is not None:
    sqs = boto3.resource('sqs')
    queue = sqs.Queue(queue_name)
    while True:
        print('sleeping 10')
        time.sleep(10)
        messages = queue.receive_messages(
            MaxNumberOfMessages=10,
            WaitTimeSeconds=20,
        )
        if not messages:
            break
        for message in messages:
            print('message', message)
            print('body', message.body)
            print('handle', message.receipt_handle)
            queue.delete_messages(
                Entries=[
                    {
                        'Id': f'id-{handled}',
                        'ReceiptHandle': message.receipt_handle
                    }
                ]
            )
            handled += 1
    print('Exiting task')
    print(f'Handled {handled} messages')
