
**Add your AWS Credentials**

`ARG AWS_SECRET_ACCESS_KEY=your-aws-secret-access-key`

`ARG AWS_ACCESS_KEY=your-aws-access-key`

**Build the image and run the container**

Remember to change `your-project-path`

docker build -t python-aws . && docker run --name super-duper-messy -v your-project-path/src:/app/src python-aws
