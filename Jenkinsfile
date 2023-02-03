pipeline{

    environment {
        registry = "takudan03/hobbie-app"
        registryCredential = credentials("jenkins-user-for-dockerhub-artifact-repository")
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
                dir('hobbie-app-server'){
                    script {
                        dockerImage = docker.build("$env.registry")
                    }
                }
            }
        }
        
        stage('Test'){
            steps{
                echo "Testing.."
                script{
                    dockerImage.withRun("-e PATH=/opt/java/openjdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"){c ->
                        sh "docker exec ${c.id} pytest -v tests/test_flask.py | tee test_results.log"
                    }
                }
            }
        }
        stage('Deploy'){
            steps{
                echo "Deploying app to artifact repository.."
                
                // Push new image to DockerHub
                script {
                    sh "docker login --username $registryCredential_USR --password $registryCredential_PSW"
                    sh "docker push ${registry}"
                }
                // this is where you would implement some way to deployment to K8S cluster...
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'test_results.log', fingerprint: true
            sh "docker logout"
            echo "The pipeline has completed"
        }
    }
}
