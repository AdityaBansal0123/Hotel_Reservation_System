pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = "rare-bastion-464310-r6"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
    }

    stages {

        stage('Clone Repository') {
            steps {
                echo "Cloning Repository..."
                checkout scmGit(
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        credentialsId: 'github-token',
                        url: 'https://github.com/AdityaBansal0123/Hotel_Reservation_System.git'
                    ]]
                )
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                echo "Setting up Virtual Environment..."
                
                sh '''#!/bin/bash
                set -e

                echo "Creating Virtual Environment..."
                python3 -m venv ${VENV_DIR}

                echo "Activating Virtual Environment & Installing dependencies..."
                source ${VENV_DIR}/bin/activate

                pip install --upgrade pip
                pip install -r requirements.txt
                pip install -e .
                '''
            }
        }

        stage('Build & Push Docker Image to GCR') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {

                    sh '''#!/bin/bash
                    set -e

                    echo "Setting PATH for gcloud..."
                    export PATH=$PATH:${GCLOUD_PATH}

                    echo "Authenticating with GCP..."
                    gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                    gcloud config set project ${GCP_PROJECT}

                    echo "Configuring Docker for GCR..."
                    gcloud auth configure-docker --quiet

                    echo "Building Docker Image..."
                    docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .

                    echo "Pushing Docker Image..."
                    docker push gcr.io/${GCP_PROJECT}/ml-project:latest
                    '''
                }
            }
        }
    }
}
pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = "rare-bastion-464310-r6"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
    }

    stages {

        stage('Clone Repository') {
            steps {
                echo "Cloning Repository..."
                checkout scmGit(
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        credentialsId: 'github-token',
                        url: 'https://github.com/AdityaBansal0123/Hotel_Reservation_System.git'
                    ]]
                )
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                echo "Setting up Virtual Environment..."
                
                sh '''#!/bin/bash
                set -e

                echo "Creating Virtual Environment..."
                python3 -m venv ${VENV_DIR}

                echo "Activating Virtual Environment & Installing dependencies..."
                source ${VENV_DIR}/bin/activate

                pip install --upgrade pip
                pip install -r requirements.txt
                pip install -e .
                '''
            }
        }

        stage('Build & Push Docker Image to GCR') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {

                    sh '''#!/bin/bash
                    set -e

                    echo "Setting PATH for gcloud..."
                    export PATH=$PATH:${GCLOUD_PATH}

                    echo "Authenticating with GCP..."
                    gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                    gcloud config set project ${GCP_PROJECT}

                    echo "Configuring Docker for GCR..."
                    gcloud auth configure-docker --quiet

                    echo "Building Docker Image..."
                    docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .

                    echo "Pushing Docker Image..."
                    docker push gcr.io/${GCP_PROJECT}/ml-project:latest
                    '''
                }
            }
        }
    }
}
