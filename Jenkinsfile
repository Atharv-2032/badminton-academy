pipeline {
    agent any

    

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
        stage('SonarCloud Analysis') {
            steps {
                withSonarQubeEnv('SonarCloud') {
                    bat "${tool 'SonarScanner'}\\bin\\sonar-scanner.bat"
                }
            }
        
        }
        stage('OWASP Dependency Check')  {
            steps {
                dependencyCheck additionalArguments: '''
                    --scan .
                    --format HTML
                    --out reports
                ''', odcInstallation: 'OWASP-DC'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t badminton_academy .'
            }
        }
         stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'docker-PAT',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    bat "docker login -u %DOCKER_USER% -p %DOCKER_PASS%"

                    bat "docker tag badminton_academy %DOCKER_USER%/badminton_academy:latest"

                    bat "docker push %DOCKER_USER%/badminton_academy:latest"
                }
            }
        }


} 
}  