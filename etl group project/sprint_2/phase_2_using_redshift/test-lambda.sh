# Copy a file into the deployed raw data bucket
# This should trigger the lambda
# The file name varies on every run of the script

team_name="where-have-you-bean"
data_bucket_name="${team_name}-csv-data-bucket" #change this
date_time=`date +%m-%d-%Y_%H-%M-%S`
new_file_name="chesterfield_${date_time}.csv"

echo ""
echo "-------------------Sending template file to S3 bucket ${data_bucket_name}...-------------------"
echo ""
aws s3 cp "chesterfield_25-08-2021_09-00-00.csv" \
  "s3://${data_bucket_name}/${new_file_name}" \
  --profile generation-de;
echo ""
echo "...Proceess complete. Please check logs for more info."
