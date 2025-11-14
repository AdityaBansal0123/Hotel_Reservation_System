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
                sh '''
                    echo "Creating Virtual Environment..."
                    python3 -m venv ${VENV_DIR}

                    echo "Activating Virtual Environment & Installing dependencies..."
                    source ${VENV_DIR}/bin/activate

                    pip install --upgrade pip

                    # Install requirements properly
                    pip install -r requirements.txt

                    # Install local package
                    pip install -e .
                '''
            }
        }

        stage('Build & Push Docker Image to GCR') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    sh '''
                        echo "Activating GCP Service Account..."
                        export PATH=$PATH:${GCLOUD_PATH}

                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                        gcloud config set project ${GCP_PROJECT}

                        echo "Configuring Docker for GCR..."
                        gcloud auth configure-docker --quiet

                        echo "Building Docker Image..."
                        docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .

                        echo "Pushing Docker Image to GCR..."
                        docker push gcr.io/${GCP_PROJECT}/ml-project:latest
                    '''
                }
            }
        }
    }
}
