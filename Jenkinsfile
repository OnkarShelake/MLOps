
pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Evidently Report') {
            steps {
                bat 'python evidently_report.py'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'evidently_report.html',
                             allowEmptyArchive: true
        }

        success {
            echo 'Build Successful!'
        }

        failure {
            echo 'Build Failed!'
        }
    }
}
