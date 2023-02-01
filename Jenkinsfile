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
                sh "echo $PATH"
                dir('hobbie-app-server'){
                    script {
                        dockerImage = docker.build("$env.registry")
//                         dockerImage.withRun("-e PATH=/opt/java/openjdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"){c ->
// //                             sh 'pwd'
// //                             sh 'whoami'
//                         }
                    }
                }
            }
        }
        
        stage('Test'){
            steps{
                echo "Testing.."
                script{
                    dockerImage.withRun("-e PATH=/opt/java/openjdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"){c ->
                        sh 'pwd'
                        // The above shows that the odcker container is running in detached mode and we are still in the jenkins container. We can access the container ID using the c parameter
                        sh "docker exec ${c.id} pytest tests/test_flask.py"
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
