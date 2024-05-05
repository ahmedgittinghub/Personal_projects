# Example IaC files for Redshift

This folder contains a full set of lambda and IaC files for deploying:

- Deployment Bucket
- Lambda with psycopg2 dependencies bundled with it
- Data bucket for CSV files
- Event trigger for lambda from S3

## Deploying

First log into AWS in your terminal.

Open a terminal in this folder (i.e `./example_code_for_redshift`).

Then, run the following:

```sh
./deploy-ci.sh
```

Then to trigger the lambda by copying a file to the S3 raw data bucket, run this:

```sh
./test-etl-lambda.sh
```
