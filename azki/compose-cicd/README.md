## Provided Description

This is a simple project to get user ip.
It is tested with python3.8 successfully.

Install the dependencies and run `python3 -m flask run`.

This app is require a mysql database to connect to it. The information is hard coded in the source file. It will be awesome if those sensitive information are read from ENV VARs and removed from source code.

Create a pipeline which build and deploy the app with docker-compose when we create a tag with trailling `-stable`. 


## Challanges

1. Dockerize the application
2. Run the application with docker-compose
3. Setup CICD pipeline with GitlabCI
  1. Register gitlab-runner that installed on the target vm. 
  2. Basic pipeline with build & deploy stages
  3. The pipeline should trigger by tags
  4. Deploy with docker-compose
4. Change the code to fill database connection string with ENV
For this, there is two solution
1. Filling ENV from docker-compose hard-coded variables
2. Using Gitlab variables to fill the ENV
https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5
