Here's a table with a detailed explanation of the underlying API calls made by Glue DynamicFrame methods in version 3:

Method	API Call
from_options	boto3.client('dynamodb').describe_table(TableName=<table_name>) - retrieves information about the table such as the primary key and attribute names.
toDF	boto3.client('dynamodb').scan(TableName=<table_name>, Limit=<limit>) or boto3.client('dynamodb').query(TableName=<table_name>, KeyConditionExpression=<condition>) - retrieves all the data in the DynamoDB table based on either a full scan or a query based on a specific condition.
filter	boto3.client('dynamodb').scan(TableName=<table_name>, Limit=<limit>, FilterExpression=<filter_expression>) or boto3.client('dynamodb').query(TableName=<table_name>, KeyConditionExpression=<condition>, FilterExpression=<filter_expression>) - retrieves data that meets the specified filter condition based on either a full scan or a query based on a specific condition.
join	boto3.client('dynamodb').scan(TableName=<table_name>, Limit=<limit>) or boto3.client('dynamodb').query(TableName=<table_name>, KeyConditionExpression=<condition>) - retrieves the data from both tables based on either a full scan or a query based on a specific condition.
Note: <table_name> is the name of the DynamoDB table, <limit> is the number of items to retrieve, <condition> is the condition to retrieve data based on, and <filter_expression> is the filter expression for filtering data.

It's important to note that Glue may perform optimizations under the hood to minimize the number of API calls made to DynamoDB, and the actual API calls made may depend on the specific version of Glue and the exact configuration of the job.