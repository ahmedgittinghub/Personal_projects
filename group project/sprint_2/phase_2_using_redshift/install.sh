#### CONFIGURATION SECTION ####
team_name="where-have-you-bean"
deployment_bucket="${team_name}-deployment-bucket"
aws_profile="generation-de"
### CONFIGURATION SECTION ####

#Step 1: Set up the deployment bucket:
echo " "
echo "------------------------------------------------\ Step 1: Creating deployment bucket \----------------------------------------"
aws cloudformation deploy --stack-name ${team_name}-deployment-bucket \
    --template-file deployment-bucket-stack.yml --region eu-west-1 \
    --capabilities CAPABILITY_IAM --profile ${aws_profile};


# Step 2: Install lambda dependencies:
echo " "
echo "----------------------------------------------\ Step 2: Installing lambda dependencies \-------------------------------------"
echo " "
py -m pip install --platform manylinux2014_x86_64 \
            --target=./src --implementation cp --python-version 3.9 \
            --only-binary=:all: --upgrade -r requirements.txt;


# #Step 3: Package up the lambda and cloud formation template:
echo " "
echo " "
echo "------------------------------------------\ Step 3: Packaging files and Cloud formation template \----------------------------"
aws cloudformation package --template-file cloud_formation.yml \
    --s3-bucket ${deployment_bucket} \
    --output-template-file lambda-stack-packaged.yml \
    --profile ${aws_profile};


# #Step 4: Deploy the packaged lambda and template:
echo " "
echo "---------------------------------------------\ Step 4: Deploying the packaged lambda and template \---------------------------"
echo " "
aws cloudformation deploy --stack-name ${team_name}-etl-app \
    --template-file lambda-stack-packaged.yml --region eu-west-1 \
    --capabilities CAPABILITY_IAM \
    --profile ${aws_profile};
echo " "
echo "------------------------------------------\ Process complete! \--------------------------------------------------------------"