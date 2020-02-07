#!/bin/bash -xe
aws cloudformation create-stack \
  --stack-name $1 \
  --template-body file://templates/baseline.template.yaml \
  --capabilities CAPABILITY_IAM \
  --region us-east-1
