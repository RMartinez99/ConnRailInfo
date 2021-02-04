node{
    
    stage('GitHub Checkout'){
        git branch: 'dev-unstable', url: 'https://github.com/RMartinez99/ConnRailInfo'
    }
    
    stage('Making sure the parts work'){
        
        'python3 test.py'
        
    }
    
    
    stage('Piecing it together...'){
        sh 'docker build -t connrailinfo .'
    
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
            sh "ssh -o StrictHostKeyChecking=no ec2-user@52.3.241.42 ${dockerRm}"
            sh "ssh -o StrictHostKeyChecking=no ec2-user@52.3.241.42 ${dockerRmI}"
            sh "ssh -o StrictHostKeyChecking=no ec2-user@52.3.241.42 ${dockerRun}"
           
        }
    
    }   
}