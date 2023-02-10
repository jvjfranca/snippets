provider "aws" {
  region = "sa-east-1"
}

resource "aws_lambda_function" "example_lambda" {
  function_name = "example_lambda"
  handler = "index.lambda_handler"
  runtime = "python3.8"

  role = aws_iam_role.example_role.arn
  timeout = 300
  memory_size = 128
  source_code_hash = filebase64sha256("example_lambda.zip")

  environment {
    variables = {
      EXAMPLE_VAR = "example_value"
    }
  }
}

resource "aws_iam_role" "example_role" {
  name = "example_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_eventbridge_rule" "example_rule_1_hour" {
  name = "example_rule_1_hour"
  description = "An example rule with a 1-hour interval"
  event_pattern = jsonencode({
    "source": [
      "aws.events"
    ],
    "detail-type": [
      "Scheduled Event"
    ]
  })
  schedule_expression = "rate(1 hour)"

  is_enabled = true
}

resource "aws_eventbridge_rule" "example_rule_2" {
  name = "example_rule_2"
  description = "An example rule with a manual trigger"
  event_pattern = jsonencode({
    "source": [
      "example.source"
    ],
    "detail-type": [
      "example.type"
    ]
  })

  is_enabled = true
}

resource "aws_lambda_event_source_mapping" "example_lambda_event_source_mapping_1" {
  event_source_arn = aws_eventbridge_rule.example_rule_1_hour.arn
  function_name = aws_lambda_function.example_lambda.function_name
}

resource "aws_lambda_event_source_mapping" "example_lambda_event_source_mapping_2" {
  event_source_arn = aws_eventbridge_rule.example_rule_2.arn
  function_name = aws_lambda_function.example_lambda.function_name
}
