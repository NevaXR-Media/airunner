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
    python_requires=">=3.7",
    description="AI Runner library",
    author="Berkay Sargın",
    author_email="berkay@nevaxr.com",
    url="https://github.com/nevaxr/ai-runner",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={
        "AIRunner": ["py.typed", "**/*.py"],
        "AIRunner.SuperNeva": ["**/*.py"],
        "AIRunner.Types": ["**/*.py"],
    },
    include_package_data=True,
)
