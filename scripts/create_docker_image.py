#!/usr/bin/env python3.10
import os
import time
import re

# get token from ECR
def  get_token_ecr():
    os.system("aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 635182717371.dkr.ecr.us-east-2.amazonaws.com/example")
    return None

# create docker build
def create_docker_build():
    # set working directory  /home/user/jenkins/example/scripts
    os.chdir("/home/user/jenkins/example/scripts")
    
    # get token from ECR with the function get_token_ecr()
    get_token_ecr()
    ecr_url = "635182717371.dkr.ecr.us-east-2.amazonaws.com/example"
    
    # create a tag with the date
    tag = time.strftime("%Y%m%d%H%M%S")
    
    
    ## create a file scripts/app/version.txt with the tag
    with open("./app/version.txt", "w") as f:
        f.write(tag)
        f.close()

    ## create docker build using Dorckerfile
    os.system("docker build -t nginx:latest .")
    
    
    # tag the image use date instead of latest
    os.system("docker tag nginx:latest {}:nginx-{}".format(ecr_url,tag))
    
    
    # upload the image to ECR
    os.system("docker push {}:nginx-{}".format(ecr_url,tag))
    return tag

# modify the terraform var
def modify_terraform_var():
    # set working directory /home/user/jenkins/example/
    os.chdir("/home/user/jenkins/example/")
    
    
    ## read the ../terraform/vars.tf file
    with open("vars.tf", "r") as f:
        data = f.read()
        
    ## find the word that start with "nginx-"
    pattern = re.compile(r'nginx-.*')
    
    
    ## replace the word with the new tag
    tag = create_docker_build()
    
    
    # create data writing nginx- + tag
    data = pattern.sub("nginx-{}\"".format(tag), data)
    

    ## write the new data to the file
    # set working directory /home/user/jenkins/example/
    os.chdir("/home/user/jenkins/example/")
    
    # write the new data to the file
    with open("vars.tf", "w") as f:
        f.write(data)
        print(data)
        f.close()
    return tag

# call the function modify_terraform_var()
modify_terraform_var()