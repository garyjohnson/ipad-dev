import boto3
import botocore

ec2 = boto3.client('ec2')
sns = boto3.client('sns')

def handle(event, context):
    name = event.get('instance-name', None)
    if not name:
        message = 'No instance-name specified. Event data: {}'.format(event)
        print(message)
        return { 'message':  message }

    reservations = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Name', 'Values': [name]},
        ]
    ).get('Reservations', [])

    instances = sum(
        [
            [i for i in r['Instances']] for r in reservations
        ], [])

    print("Found {} instances that need starting".format(len(instances)))
    instance_ids = [i['InstanceId'] for i in instances]
    print("Starting {}".format(instance_ids))

    try:
        ec2.start_instances(InstanceIds=instance_ids)
        return { 'message': 'Started EC2 instances: {}'.format(instance_ids) }
    except Exception as e:
        message = "Error while starting {}".format(e)
        print(message)
        return { 'message': message }

