import boto3

'''
PARAMS

ImageId='ami-00000eba05d89f9dd', InstanceType='t2.micro', MinCount=1, MaxCount=1
'''


class EC2ServiceManager:

    def __init__(self, **kwargs):
        self.client = boto3.client('ec2')
        self.params = kwargs
        self.instances = []

    def get_all_ec2(self, **filters):
        resp = self.client.describe_instances(**filters)
        for reservation in resp['Reservations']:
            for instance in reservation['Instances']:
                self.instances.append(instance['InstanceId'])

    def launch_ec2(self):
        resp = self.client.run_instances(**self.params)
        for instance in resp['Instances']:
            self.instances.append(instance['InstanceId'])

    def stop_all_ec2(self):
        return self.client.stop_instances(InstanceIds=self.instances)

    def start_all_ec2(self):
        return self.client.start_instances(InstanceIds=self.instances)

    def terminate_all_ec2(self):
        return self.client.terminate_instances(InstanceIds=self.instances)
