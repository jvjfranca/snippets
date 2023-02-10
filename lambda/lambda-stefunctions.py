import boto3

def lambda_handler(event, context):
    client = boto3.client("stepfunctions")
    
    step_function_A = "arn:aws:states:sa-east-1:<ACCOUNT_ID>:stateMachine:step_function_A"
    step_function_B = "arn:aws:states:sa-east-1:<ACCOUNT_ID>:stateMachine:step_function_B"
    step_function_C = "arn:aws:states:sa-east-1:<ACCOUNT_ID>:stateMachine:step_function_C"
    
    # Check if there is an execution running for step function A
    response = client.list_executions(
        stateMachineArn=step_function_A,
        statusFilter="RUNNING"
    )
    
    if len(response["executions"]) > 0:
        # An execution is already running for step function A
        return

    # Check if there is an execution running for step function B
    response = client.list_executions(
        stateMachineArn=step_function_B,
        statusFilter="RUNNING"
    )
    
    if len(response["executions"]) > 0:
        # An execution is already running for step function B
        return

    # Check if there is an execution running for step function C
    response = client.list_executions(
        stateMachineArn=step_function_C,
        statusFilter="RUNNING"
    )
    
    if len(response["executions"]) > 0:
        # An execution is already running for step function C
        return

    # If none of the step functions are running, start the execution of step function A
    client.start_execution(
        stateMachineArn=step_function_A
    )
