import boto3
from botocore.config import Config


poly = boto3.client('polly',config=Config(region_name='us-east-1'))
# read local text file
with open('polly_file.txt', 'r') as file_name:
    file_text = file_name.read()

def convert_text_to_audio(text):
    """
    Convert the text read using the start_speech_synthesis_task method using Joanna, SSML format etc and store output to s3 bucket
    """
    response = poly.start_speech_synthesis_task(Text= text,VoiceId='Joanna', OutputFormat='mp3',TextType='ssml', LanguageCode='en-US', Engine='neural',OutputS3BucketName='practice-buckets')

    # body=response['AudioStream'].read()

    # file_name = 'voice.mp3'

    # with open(file_name,'wb') as file_content:
    #     file_content.write(body)

if __name__ == "__main__":
    convert_text_to_audio(file_text)