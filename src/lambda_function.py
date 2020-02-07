# Given a Patch Baseline, set it to default
# Then, signal back CloudFormation a success signal

import json
import boto3
import logging
import os
import cfnresponse
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def set_baseline(mybaseline):

    ssm = boto3.client('ssm')

    logger.info(f'About to set baseline {mybaseline} as the default...')

    response = ssm.register_default_patch_baseline(
        BaselineId=mybaseline
    )

    logger.info(f'SSM response is {response}')

def signal_success():
    logger.info('Sending success response back to CloudFormation')
    responseData = {}
    responseData['Comment'] = 'example custom respone data where we could return custom attributes'
    cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData)

def signal_failure():
    logger.info('Sending FAILURE response back to CloudFormation')
    responseData = {}
    responseData['Comment'] = 'example custom respone data where we could return custom attributes'
    cfnresponse.send(event, context, cfnresponse.FAILURE, responseData)

def lambda_handler(event, context):
    logger.info('Beginning function...')
    logger.info(f'Got event: {event}')
    
    requestType = event['requestType']
    baselineId = event['ResourceProperties']['baselineId']
    logger.info(f'Request Type is: {requestType}')
    logger.info(f'Baseline ID is: {baselineId}')

    # Now set our baseline
    if requestType == "Create" or requestType == "Update":
        logger.info(f'Got a {requestType} request, setting default baseline...')
        try:
            set_baseline(baselineId)
            signal_success()
        except:
            logger.error(f'Unknown failure in setting default patch baseline!')
            signal_failure()
    else if requestType == "Delete":
        #  No good definition for "undoing" a default set
        #  TODO One option here would be to add code to set default back to the AWS Default
        logger.info('Got Delete request, doing nothing except signalling back success.')
        signal_success()
    else:
        logger.info(f'Request type is not recognized! Request Type was {requestType}')
        

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function ending.')
    }

