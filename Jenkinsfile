pipeline {
    agent any 
    stages {
        stage('Stage 1') {
            steps {
                ./manage.py jenkins --enable-coverage
            }
        }
    }
}