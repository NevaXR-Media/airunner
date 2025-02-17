import os
from setuptools import setup, find_packages

setup(
    name="airunner",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "boto3",
        "aws-sqs-consumer",
        "typing",
    ],
    author="Berkay Sargın",
    author_email="berkay@nevaxr.com",
    description="A Python library for running AI pipelines with AWS SQS integration",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/berkaysargin/ai-runner",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
)
