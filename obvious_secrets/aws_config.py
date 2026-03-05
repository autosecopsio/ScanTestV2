"""
aws_config.py — Production AWS credentials for S3 bucket operations.
WARNING: These should be loaded from env vars or IAM roles in production.
"""

import boto3

# Direct credential injection (BAD PRACTICE — should use IAM roles)
AWS_ACCESS_KEY_ID = "AKIA0BU3SLMSLYSTFH93"
AWS_SECRET_ACCESS_KEY = "PnMnQlDBnUbqxfPTGXs1lNfNaObDJi7GZ3XkK8jX"
AWS_REGION = "us-east-1"
S3_BUCKET = "autosecops-artifacts-prod"


def get_s3_client():
    return boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION,
    )


def upload_report(filepath: str, key: str):
    client = get_s3_client()
    client.upload_file(filepath, S3_BUCKET, key)
    print(f"Uploaded {filepath} to s3://{S3_BUCKET}/{key}")
