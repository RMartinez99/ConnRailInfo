pipeline {
     
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

            withCredentials([string(credentialsId: 'docker-pwd', variable: 'dockerHubPwd')]) {
                sh "docker login -u rm267 -p ${dockerHubPwd}"
    
                }
        
            sh 'docker push rm267/connrailinfo'
    
        }
        stage('Container Execution, on private EC2'){
        def dockerRm = 'docker rm -f connrailinfo'
        def dockerRmI = 'docker rmi rm267/connrailinfo'
        def dockerRun = 'sudo docker run -it hello-demo test_Events.py'
        sshagent(['docker-server']) {
            sh "ssh -o StrictHostKeyChecking=no ec2-user@18.234.192.242 ${dockerRm}"
            sh "ssh -o StrictHostKeyChecking=no ec2-user@18.234.192.242 ${dockerRmI}"
            sh "ssh -o StrictHostKeyChecking=no ec2-user@18.234.192.242 ${dockerRun}"
           
        }
    
        }   
     }
     }