//pipeline to create a docker image and upload it to ECR using a deployment script and terraform
pipeline {
    agent any

    environment {
        // your terraform workspace
        projectworkspace =  '/var/lib/jenkins/workspace/example/'
        // your web app workspace
        appworkspace =  '/var/lib/jenkins/workspace/app-example/'
        // your remote workspace on deployment server
        remoteworkspace =  '/home/user/jenkins/example'
        // your deployment server
        remoteserver = 'user@ip'
    }

    stages {
        //get terraform code from git
        stage('Get code') {
            steps {
                git //your git repo
            }
        }
        //copy app code from git to workspace on different folder
        stage('Get app code') {
            steps {
                dir(appworkspace) {
                    git //your web app git repo
                }
            }
        }
        //copy terraform code from git to workspace.
        stage('Copy terraform code') {
            steps {
                sh 'rsync -auv --rsh="ssh -p32"   \$projectworkspace \$remoteserver:\$remoteworkspace'
            }
        }
        //copy app code from git to workspace
        stage('Copy app code') {
            steps {
                sh 'rsync -auv --rsh="ssh -p32" --delete-after \$appworkspace \$remoteserver:\$remoteworkspace/scripts/app/'
            }
        }
        //call python script to create the docker image on remote server
        stage('Create docker image and upload to ECR') {
            steps {
            sh """ssh -i /var/lib/jenkins/.ssh/id_rsa -p 32 \$remoteserver  '/usr/bin/python3 '\$remoteworkspace'/scripts/create_docker_image.py'"""
            }
        }
        // fmt terraform code
        stage('fmt terraform code') {
            steps {
                sh "ssh -i /var/lib/jenkins/.ssh/id_rsa -p 32 \$remoteserver 'cd ' \$remoteworkspace '&& /usr/bin/terraform fmt -recursive'"
            }
        }
        // init terraform code
        stage('init terraform code') {
            steps {
                sh "ssh -i /var/lib/jenkins/.ssh/id_rsa -p 32 \$remoteserver 'cd ' \$remoteworkspace '&& /usr/bin/terraform init'"
            }
        }
        // validate terraform code
        stage('validate terraform code') {
            steps {
                sh "ssh -i /var/lib/jenkins/.ssh/id_rsa -p 32 \$remoteserver 'cd ' \$remoteworkspace  '&& /usr/bin/terraform validate'"
            }
        }

        // plan terraform code
        stage('plan terraform code') {
            steps {
                sh "ssh -i /var/lib/jenkins/.ssh/id_rsa -p 32 \$remoteserver 'cd ' \$remoteworkspace  '&& /usr/bin/terraform plan -out=plan.out'"
            }
        }

        // apply terraform code
        stage('apply terraform code') {
            steps {
                sh "ssh -i /var/lib/jenkins/.ssh/id_rsa -p 32 \$remoteserver 'cd ' \$remoteworkspace '&&  /usr/bin/terraform apply -auto-approve plan.out'"
            }
        }
    }
}

