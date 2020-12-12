import boto3

from transform_post import return_total_clean_content

#get the clean data and store in a local file
content = return_total_clean_content()
with open('polly_file.txt', 'w') as file_name:
    file_name.write(content)

print('Done')

#to store in s3
# s3 = boto3.client('s3')
# bucket_name = 'practice-buckets'
# key = 'input_files/clean_medium_post.txt'
# s3.put_object(Bucket=bucket_name,Key=key,Body=content)

