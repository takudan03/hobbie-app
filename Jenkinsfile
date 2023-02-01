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
                def agentPath = "/opt/java/openjdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
                dir('hobbie-app-server'){
                    script {
                        docker.build("$env.registry").inside("-e PATH=${agentPath}"){
                            sh 'pwd'
                            sh 'whoami'
//                         sh 'pytest tests/test_flask.py'
                        }
                    }
                }
            }
        }
        
        stage('Test'){
            steps{
                echo "Testing.."
                script{
                    docker.withTool('my_docker_installation'){
                        docker.image("$env.registry").pull().run { c->
                            sh 'pytest tests/test_flask.py'
                            sh "docker logs ${c.id}"
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
