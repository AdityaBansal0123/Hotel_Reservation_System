pipeline {
    agent any

    environment {
        PYTHON = "python3"
        VENV = "venv"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo "Fetching code from GitHub..."
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/AdityaBansal0123/Hotel_Reservation_System.git',
                        credentialsId: 'github-token'
                    ]]
                ])
            }
        }

        stage('Create Virtual Environment & Install Dependencies') {
            steps {
                sh '''
                    echo "Setting up Python virtual environment..."
                    ${PYTHON} -m venv ${VENV}
                    . ${VENV}/bin/activate

                    echo "Upgrading pip..."
                    pip install --upgrade pip

                    echo "Installing project dependencies..."
                    pip install -e .
                '''
            }
        }

        stage('Run ML Pipeline') {
            steps {
                sh '''
                    echo "Running ML pipeline..."
                    . ${VENV}/bin/activate
                    python main.py
                '''
            }
        }

        /* 
        Optional — for running Flask API inside Jenkins.
        Uncomment only if needed.
        stage('Run Flask Server') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    export FLASK_APP=app.py
                    nohup flask run --host=0.0.0.0 --port=5000 &
                '''
            }
        }
        */

        stage('Archive Artifacts') {
            steps {
                echo "Archiving model and logs..."
                archiveArtifacts artifacts: 'artifacts/**', fingerprint: true
            }
        }
    }

    post {
        success {
            echo "🎉 Pipeline finished successfully!"
        }
        failure {
            echo "❌ Pipeline failed! Check logs."
        }
    }
}
