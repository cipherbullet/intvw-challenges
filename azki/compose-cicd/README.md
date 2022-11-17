## Provided Description

This is a simple project to get user ip.
It is tested with python3.8 successfully.

Install the dependencies and run `python3 -m flask run`.

This app is require a mysql database to connect to it. The information is hard coded in the source file. It will be awesome if those sensitive information are read from ENV VARs and removed from source code.

Create a pipeline which build and deploy the app with docker-compose when we create a tag with trailling `-stable`. 


## Challanges

### Dockerize the application
Separate COPY command for requirements.txt and src directory and put pip installation command between them. It will helps to improve docker layer caching and increases image build speed for next runs. 
Note that the application will run on port 5000


### Run the application with docker-compose
Try to not map mysql ports. because the connection of app and mysql can be handled from docker network(I used bridge mode), there is no need to bind mysql port for external access.

### Setup CICD pipeline with GitlabCI
  1. Register gitlab-runner that installed on the target vm. 
  2. Basic pipeline with build & deploy stages
  3. The pipeline should trigger by tags ($CI_COMMIT_TAG var)
  4. Deploy with docker-compose
  5. Change pipeline to just run `stable` appended tags
  ```
    job:
        only:
            refs:
                - tags
            variables:
                - $CI_BUILD_REF_NAME =~ /-stable$/
  ```
  

### Change the code to fill database connection string with ENV
Follow [this link](https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5) guide for python env variables.
For this, there is two solution
1. Filling ENV from docker-compose hard-coded variables(I did that)
2. Using Gitlab variables to fill the ENV
