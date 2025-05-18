pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Build Docker Images') {
            steps {
                dir('task_manager') {
                    sh 'docker-compose build'
                }
            }
        }

        stage('Deploy Containers') {
            steps {
                dir('task_manager') {
                    sh 'docker-compose up -d'
                }
            }
        }
    }
}