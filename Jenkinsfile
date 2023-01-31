pipeline{

    environment {
        registry = "takudan03/hobbie-app"
        registryCredential = 'takudan03'
        dockerImage = ''
    }

    agent any
//     agent {
//         docker {
//             image 'takudan03/hobbie-app'
//         }
//     }

    stages {
        stage('build'){
            steps{
                echo "Building image from SC.."
                script {
                    dockerImage = docker.build registry
                }
            }
        }
        
        stage('Test'){
            steps{
                echo "Testing.."
                script{
                    dockerImage.inside{
                        sh 'pytest tests/test_flask.py'
                    }
                }
            }
        }
        stage('Deploy'){
            steps{
                echo "Deploying app to artifact repository.."
                // script {
                //     docker.withRegistry( '', registryCredential ) {
                //         dockerImage.push()
                //     }
                // }
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
