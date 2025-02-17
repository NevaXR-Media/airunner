from setuptools import setup, find_packages

setup(
    name="air",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "boto3",
        "aws-sqs-consumer",
        "typing",
        "requests",
    ],
    python_requires=">=3.11",
    description="AI Runner Library",
    author="Berkay Sargın",
    author_email="berkay@nevaxr.com",
    url="https://github.com/nevaxr/ai-runner",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={
        "air": ["**/*.py"],
        "air.AIRunner": ["**/*.py"],
        "air.SuperNeva": ["**/*.py"],
        "air.Types": ["**/*.py"],
    },
    include_package_data=True,
)
