# Github_To_S3

A python utility to help you deploy your github files to S3 bucket via AWS Lambda

## Motivation

I started this project, while I was working on a React APP that was hosted on S3, and it was quite tedious to update files everytime we pushed code.

## Usage

1. Setup AWS SNS service for your github repository
2. Setup AWS lambda. You must include the following environment variables. All the environemnt variables are required except that are marked optional.
    
    * set `main.setup` as the Handler
    * set `AWS_BUCKET` environment variable. This is the name of your s3 bucket where'd you want to deploy the code
    * set `AWS_REGION_NAME` environment variable. This is your aws region of your bucket
    * set `CONTENT_PATH`(optional) if you want to deploy files from a particular directory in your github project. If you just want to deploy build files that are in the build directory of the root, then set value as `build`
    * set `GITHUB_REPO` environment variable. This is the name of the repo. **Note:** Don't include the github username. Set `example_repo` instead of `example_user/example_repo`.
    * set `GITHUB_TOKEN` environment variable. Your github personal access token with at least `repo_deployment` scope enabled.
    * set `GITHUB_USER` environment variable. Your github username.
    * set `aws_access_key_id`. The AWS ACCESS KEY with at least read & write access to s3.
    * set `aws_secret_access_key`. The AWS ACCESS SECRET with at least read & write access to s3.
    * set `branch`. The github branch from which you'd want to deploy the code.
3. If you have executed `build.sh` you'd see `github_to_s3.zip` file in your directory, upload it to lambda, and save.

## Toubleshooting

Kindly make sure that you have followed the steps correctly. If you are still facing any issue then please open an issue, or if you are in a hurry you may contact me at [mailto:contact@ayushbahuguna.com](Ayush bahuguna)
