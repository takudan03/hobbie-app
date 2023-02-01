pipeline{

    environment {
        registry = "takudan03/hobbie-app"
        registryCredential = 'takudan03'
        dockerImage = ''
    }
    
    tools {
        'org.jenkinsci.plugins.docker.commons.tools.DockerTool' 'my_docker_installation'
    }

    agent any

    stages {
        stage('build'){
            steps{
                echo "Building image from SC.."
                script {
                    dockerImage = docker.build("$env.registry", "./hobbie-app-server/")
                }
            }
        }
        
        stage('Test'){
            steps{
                echo "Testing.."
                script{
                    docker.withTool('my-docker-installation'){ 
                        docker.image('takudan03/hobbie-app').inside{
                            sh 'pytest tests/test_flask.py'
                        }
                    }
//                     dockerImage.inside{
//                         sh 'pytest tests/test_flask.py'
//                     }
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
