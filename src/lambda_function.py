# Given a Patch Baseline, set it to default
# Then, signal back CloudFormation a success signal

import json
import boto3
import logging
import os
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def set_baseline(mybaseline)

    ssm = boto3.client('ssm')

    response = ssm.register_default_patch_baseline(
        BaselineId=mybaseline
    )

def lambda_handler(event, context):
    logger.info('Beginning function...')
    logger.info('got event{}'.format(event))
    
    # Get from event data the baseline we want to set

    # TODO Now set our baseline

    # TODO And signal back

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function ending.')
    }
