provider "aws" {
  region = "sa-east-1"
}

resource "aws_events_rule" "rule_B" {
  name = "rule_B"

  event_pattern = <<EOF
{
  "source": [
    "aws.stepfunctions"
  ],
  "detail-type": [
    "Step Functions Execution Successful"
  ],
  "detail": {
    "stateMachineArn": "arn:aws:states:sa-east-1:<ACCOUNT_ID>:stateMachine:step_function_A"
  }
}
EOF
}

resource "aws_events_rule" "rule_C" {
  name = "rule_C"

  event_pattern = <<EOF
{
  "source": [
    "aws.stepfunctions"
  ],
  "detail-type": [
    "Step Functions Execution Successful"
  ],
  "detail": {
    "stateMachineArn": "arn:aws:states:sa-east-1:<ACCOUNT_ID>:stateMachine:step_function_B"
  }
}
EOF
}

resource "aws_events_target" "target_B" {
  rule = "${aws_events_rule.rule_B.name}"
  target_id = "target_B"
  arn = "arn:aws:states:sa-east-1:<ACCOUNT_ID>:stateMachine:step_function_B"
}

resource "aws_events_target" "target_C" {
  rule = "${aws_events_rule.rule_C.name}"
  target_id = "target_C"
  arn = "arn:aws:states:sa-east-1:<ACCOUNT_ID>:stateMachine:step_function_C"
}
