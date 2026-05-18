pipeline {
    agent any

    tools {
        jdk 'JDK17'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Atharv-2032/badminton-academy.git'
            }
        }
        stage('Test') {
            steps {
                echo 'Jenkinsfile is working'
            }
        }
        
    }


}   