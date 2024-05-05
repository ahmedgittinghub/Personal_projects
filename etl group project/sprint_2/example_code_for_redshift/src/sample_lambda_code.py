from connect_to_db import *
from generate_sql_db import *
#from my_utility_functions import *
import os

ssm_env_var_name = 'SSM_PARAMETER_NAME'

def lambda_handler(event, context):
    print('lambda_handler: starting')

    try:

      ssm_param_name = os.environ[ssm_env_var_name] or 'NOT_SET'
      print(f'lambda_handler: ssm_param_name={ssm_param_name} from ssm_env_var_name={ssm_env_var_name}')

      # inspect event
      file_path = 'NOT_SET' # just here to make the exception handler compile

      #bucket_name, file_path = get_details(event)
      #print(f'lambda_handler: event: file=${file_path}, bucket_name=${bucket_name}')

      # load file from s3
      #file_object = get_file(bucket_name, file_path)
      # process file as csv
      #csv_file = do_something(file_object)
      # transform the data /clean it / reorganize
      #dict_or_list_of_data = my_transform_function(csv_file)

      # connection
      redshift_details = get_ssm_param(ssm_param_name)
      conn, cur = open_sql_database_connection_and_cursor(redshift_details)

      # run some sql
      create_db_tables(conn, cur)

      # run some sql
      #save_my_data(conn, cur, dict_or_list_of_data)

      #print(f'lambda_handler: done, file=${file_path}')

    except Exception as whoopsy:
      # ...exception reporting
      print(f'lambda_handler: boom, error=${whoopsy}, file=${file_path}')
