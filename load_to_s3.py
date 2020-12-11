import boto3

from transform_post import return_total_clean_content

content = return_total_clean_content()
s3 = boto3.client('s3')
bucket_name = 'practice-buckets'
key = 'input_files/clean_medium_post.txt'
s3.put_object(Bucket=bucket_name,Key=key,Body=content)
print('Done')
