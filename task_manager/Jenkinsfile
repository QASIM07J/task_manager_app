pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                // This is done automatically by Jenkins when pulling the repo
                echo 'Cloning repository...'
            }
        }
        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }
        stage('Deploy Containers') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}
