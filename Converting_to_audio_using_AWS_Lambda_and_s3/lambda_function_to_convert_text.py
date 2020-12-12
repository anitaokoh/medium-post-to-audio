import boto3
import json
from botocore.config import Config

def lambda_handler(event, context):
    """
    To get data from s3 as input to polly that converts to audio and stores audio to s3
    """
    s3 = boto3.client('s3')
    bucket = 'practice-buckets'
    key = 'input_files/clean_medium_data2.txt'
    file = s3.get_object(Bucket=bucket,Key=key)
    paragraph = file['Body'].read().decode('utf-8')
  
    
    
    poly = boto3.client('polly',config=Config(region_name='us-east-1'))
    
    response = poly.start_speech_synthesis_task(Text= paragraph,VoiceId='Joanna', OutputFormat='mp3',TextType='ssml', LanguageCode='en-US', Engine='neural',OutputS3BucketName='practice-buckets')
    print(event)
        
    return {
        'statusCode': 200,
        'body':json.dumps('Hello Anita')
    }