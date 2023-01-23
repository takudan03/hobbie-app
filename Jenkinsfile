pipeline{
    agent any

    stages {
        stage('build'){
            steps{
                echo "Test Building triggered by github poll.."
            }
        }
        stage('Test'){
            steps{
                echo "Testing.."
            }
        }
        stage('Deploy'){
            steps{
                echo "Deploying app.."
            }
        }

    }
}