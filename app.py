from aws_cdk import App
from aws_cdk import Stack

from constructs import Construct

from aws_cdk.aws_ecs import ContainerImage

from aws_cdk.aws_ecs_patterns import QueueProcessingFargateService

from shared_infrastructure.cherry_lab.environments import US_WEST_2
from shared_infrastructure.cherry_lab.vpcs import VPCs


class QueueStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpcs = VPCs(self, 'VPCs')

        image = ContainerImage.from_asset('.')

        fargate = QueueProcessingFargateService(
            self,
            'QueueProcessingFargateService',
            image=image,
            vpc=vpcs.default_vpc,
        )


app = App()

stack = QueueStack(
    app,
    'QueueStack',
    env=US_WEST_2
)

app.synth()
