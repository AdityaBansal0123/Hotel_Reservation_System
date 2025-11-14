pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = "rare-bastion-464310-r6"
        GCLOUD_PATH = "/usr/lib/google-cloud-sdk/bin"
        IMAGE_NAME = "ml-project"
        IMAGE_URI = "gcr.io/${GCP_PROJECT}/${IMAGE_NAME}:latest"
    }

    stages {

        stage('Clone Repository') {
            steps {
                echo "Cloning project repository..."
                checkout scmGit(
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        credentialsId: 'github-token',
                        url: 'https://github.com/AdityaBansal0123/Hotel_Reservation_System.git'
                    ]]
                )
            }
        }

        stage('Setup Python Virtual Environment') {
            steps {
                script {
                    echo "Setting up Python environment..."
                    sh """
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    """
                }
            }
        }

        stage('Authenticate GCP & Build Docker Image') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo "Authenticating with Google Cloud..."
                        
                        sh """
                        export PATH=\$PATH:${GCLOUD_PATH}

                        gcloud auth activate-service-account --key-file=\${GOOGLE_APPLICATION_CREDENTIALS}
                        gcloud config set project ${GCP_PROJECT}

                        gcloud auth configure-docker --quiet

                        echo "Building Docker image..."
                        docker build -t ${IMAGE_URI} .

                        echo "Pushing Docker image..."
                        docker push ${IMAGE_URI}
                        """
                    }
                }
            }
        }
    }
}
