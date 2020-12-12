import json
import boto3
from transform_post import return_total_clean_content

def lambda_handler(event, context):
    """
    To run the extract and transform py file and store clean text in s3. Then invoke the conversion lambda function
    """
    content = return_total_clean_content()
    s3 = boto3.client('s3')
    bucket_name = 'practice-buckets'
    key = 'input_files/clean_medium_data2.txt'
    s3.put_object(Bucket=bucket_name,Key=key,Body=content)
    
    invokelam = boto3.client('lambda',region_name='us-east-1')
    payload = {'message':'You have been invoked'}
    resp = invokelam.invoke(FunctionName = "text-to-speech", InvocationType = "Event", Payload = json.dumps(payload))
    print('Done')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }