set -eu

#### CONFIGURATION SECTION ####
team_name="Hannibals-potato"
deployment_bucket="${team_name}-deployment-bucket"
aws_profile="generation-de"
#### CONFIGURATION SECTION ####

# Create deployment bucket stack
echo "Doing deployment bucket..."
aws cloudformation deploy --stack-name ${team_name}-deployment-bucket \
    --template-file deployment-bucket-stack.yml --region eu-west-1 \
    --capabilities CAPABILITY_IAM --profile ${aws_profile};

# Install dependencies from requirements-deploy.txt into src directory with python 3.9
# On windows use `py` not `python3`
echo "Doing pip install..."
python3 -m pip install --platform manylinux2014_x86_64 \
    --target=./src --implementation cp --python-version 3.9 \
    --only-binary=:all: --upgrade -r requirements-lambda.txt;

# Package template and upload local resources to S3
# A unique S3 filename is automatically generated each time
echo "Doing packaging..."
aws cloudformation package --template-file lambda-stack.yml \
    --s3-bucket ${deployment_bucket} \
    --output-template-file lambda-stack-packaged.yml \
    --profile ${aws_profile};

# Deploy template
echo "Doing etl stack deployment..."
aws cloudformation deploy --stack-name ${team_name}-etl-app \
    --template-file lambda-stack-packaged.yml --region eu-west-1 \
    --capabilities CAPABILITY_IAM \
    --profile ${aws_profile};

echo "...all done!"
