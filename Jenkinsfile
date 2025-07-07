pipeline {
    agent {label "fast_api_node"}

    stages {
        stage('Build') {
            steps {
                echo 'Building the code'
                git url: "https://github.com/shobhit287/fastapi-server-jenkins-automate.git", branch: "prod"
                sh "docker build -t fast_api_image:latest ."
            }
        }
        
        stage("Push") {
            steps {
                echo "Pushing the image to docker hub"
                withCredentials([
                    usernamePassword(
                        credentialsId: "dockerHub-cred",
                        usernameVariable: "DOCKER_USER",
                        passwordVariable: "DOCKER_PASSWORD")]) {
                            sh '''
                                echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USER" --password-stdin
                                docker tag fast_api_image:latest "$DOCKER_USER/fast_api_image:latest"
                                docker push "$DOCKER_USER/fast_api_image:latest"
                            '''
                        }
            }
        }
        stage("Deploy") {
            steps {
                echo "Deploying"
                sh "docker-compose down"
                sh "docker-compose up -d "
                echo "Deployment successfull"
            }
        }
    }
}
