locals {
	lambda_name = "scraper_api"
}
# Managed Policies
data "aws_iam_policy_document" "assume_role_lambda" {
	statement {
		effect = "Allow"
	}

	principals {
		type = "Service"
		identifiers = [ "lambda.amazonaws.com" ]
	}

	actions = [ "sts:AssumeRole" ]
}


### Policy Documents
data "aws_iam_policy_document" "lambda_logging" {
  statement {
    effect = "Allow"

    actions = [
		"logs:CreateLogGroup",
		"logs:CreateLogStream",
		"logs:PutLogEvents",
    ]

    resources = [ "arn:aws:logs:*:*:*" ]
  }
}

####Policies
resource "aws_iam_policy" "lambda_logging" {
	name = "lambda_logging"
	path  = "/"
	description = "IAM policy for logging from a lambda"
	policy = data.aws_iam_policy_document.lambda_logging.json
}


###### IAM Roles
resource "aws_iam_role" "iam_for_lambda" {
	name = "iam_assume_role_for_lambda"
	assume_role_policy = data.aws_iam_policy_document.assume_role_lambda.json
}

resource "aws_iam_role_policy_attachment" "lambda_logging" {
	role = aws_iam_role.iam_for_lambda.name
	policy_arn = aws_iam_policy.lambda_logging.arn
}

#### Lambda Source Code

data "archive_file" "lambda" {
	type = "zip"
	source_file = "path_to_code"
	output_path = "./functions/lambda_function.zip"
}

#### Resources

resource "aws_cloudwatch_log_group" "example" {
	name = "/aws/lambda/${local.lambda_name}"
	retention_in_days = 14
}

#### Lambdas

####### Layer? ########

resource "aws_lambda_function" "scraper-api-lambda" {
	filename = "../backend/main.py"
	function_name = local.azs
	role = aws_iam_role.iam_for_lambda.arn
	handler = "main.handler"

	source_code_hash = data.archive_file.lambda.output_base64sha256

	runtime = "python3.9"

	environment {
		variables = {}
	}

	ephemeral_storage {
		size = 512 # default is 512 MB, max is 10240
	}

	tags = {
		Name = "scraper-api"
	}

	depends_on = [
	  aws_iam_role.iam_for_lambda
	]
}