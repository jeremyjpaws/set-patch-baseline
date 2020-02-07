# Given a Patch Baseline, set it to default
# Then, signal back CloudFormation a success signal

import json
import boto3
import logging
import os
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def set_baseline(mybaseline):

    ssm = boto3.client('ssm')

    logger.info(f'About to set baseline {mybaseline} as the default...')

    response = ssm.register_default_patch_baseline(
        BaselineId=mybaseline
    )

    logger.info(f'SSM response is {response}')

def lambda_handler(event, context):
    logger.info('Beginning function...')
    logger.info(f'got event: {event}')
    
    # Get from event data the baseline we want to set
    baselineId = event["baseline"]
    logger.info(f'Baseline ID is: {baselineId}')

    # TODO Now set our baseline
    set_baseline(baselineId)

    # TODO And signal back

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function ending.')
    }
