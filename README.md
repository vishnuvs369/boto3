# boto3

install the new version of boto3. This will also install botocore.

$ python3 -m pip install boto3

you can optionally verify that the freshly installed copy of Boto3 is using the correct version of Python.

$ python3 -c "import boto3, sys; print(f'{sys.version} \nboto3: {boto3.__version__}')"

