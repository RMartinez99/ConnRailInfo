pipeline {
     agent { docker { image 'python:3.7.9' }}
     stages {
         
         stage('Making Sure the parts work') {
             steps {
                 withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'python3 test.py'
                 }
             }
         }
         stage('Loading onto Docker'){
             steps{
                 sh 'docker build -t connrailinfo .'

             }

         }
        stage('Sailing off to Docker...'){
            steps{
                withCredentials([string(credentialsId: 'docker-pwd', variable: 'dockerHubPwd')]) {
                    sh "docker login -u rm267 -p placeholder"
        
                    }
            
                sh 'docker push rm267/connrailinfo'
            }
        }
        stage('Container Execution, on private EC2'){
            steps{
                
                sshagent(['docker-server']) {
                    sh "ssh -o StrictHostKeyChecking=no ec2-user@18.234.192.242 docker rm -f connrailinfo"
                    sh "ssh -o StrictHostKeyChecking=no ec2-user@18.234.192.242 docker rmi rm267/connrailinfo"
                    sh "ssh -o StrictHostKeyChecking=no ec2-user@18.234.192.242 sudo docker run -it hello-demo test.py"
                
                }
        
            } 
        }  
     }
}
