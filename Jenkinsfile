
pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
                echo 'Code fetched from GitHub'
            }
        }

        stage('Check Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    if exist .venv rmdir /s /q .venv
                    python -m venv .venv
                    .venv\\Scripts\\python -m pip install --upgrade pip
                    .venv\\Scripts\\python -m pip install -r requirements.txt
                    .venv\\Scripts\\python -m pip show pandas evidently
                '''
                }
        }

        stage('Run Pytest') {
            steps {
                bat '.venv\\Scripts\\python -m pytest -v'
            }
        }

        stage('Evidently Report') {
            steps {
                bat '.venv\\Scripts\\python evidently_report.py'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'evidently_report.html',
                             allowEmptyArchive: true
        }

        success {
            echo 'MLOps Pipeline Completed Successfully!'
        }

        failure {
            echo 'MLOps Pipeline Failed!'
        }
    }
}
