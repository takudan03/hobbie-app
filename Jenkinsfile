pipeline{

    environment {
        registry = "takudan03/hobbie-app"
        registryCredential = 'takudan03'
        dockerImage = ''
    }

    agent any

    stages {
        stage('build'){
            steps{
                echo "Building image from SC.."
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Test'){
            steps{
                echo "Testing.."
                sh "pytest hobbie-app-server/tests/test_flask.py"
            }
        }
        stage('Deploy'){
            steps{
                echo "Deploying app to artifact repository.."
                docker.withRegistry( '', registryCredential ) {
                    dockerImage.push()
                }
                // Deployment to K8S cluster...
            }
        }
    }

    post {
        always {
            echo "The pipeline has completed"
        }
    }
}