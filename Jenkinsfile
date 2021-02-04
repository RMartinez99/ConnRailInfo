node{
    
    stage('GitHub Checkout'){
        git branch: 'master', credentialsId: 'git-creds', url: 'https://github.com/RMartinez99/ConnRailInfo'
    }
    
    stage('Making sure the parts work'){
        sh 'pytest test_Functions.py'
    }
    
    stage('Piecing it together...'){
        sh 'docker build -t ConnRailInfo .'
    
    }

    stage('Sailing off to Docker...'){

        withCredentials([string(credentialsId: 'docker-pwd', variable: 'dockerHubPwd')]) {
            sh "docker login -u RMartinez99 -p ${dockerHubPwd}"
    
            }
        
        sh 'docker push RMartinez99/CT'
    
    }

    stage('Container Execution, on private EC2'){
        def dockerRm = 'docker rm -f ConnRailInfo'
        def dockerRmI = 'docker rmi RMartinez99/ConnRailInfo'
        def dockerRun = 'sudo docker run -it hello-demo test_Events.py'
        sshagent(['docker-server']) {
            sh "ssh -o StrictHostKeyChecking=no ec2-user@52.3.241.42 ${dockerRm}"
            sh "ssh -o StrictHostKeyChecking=no ec2-user@52.3.241.42 ${dockerRmI}"
            sh "ssh -o StrictHostKeyChecking=no ec2-user@52.3.241.42 ${dockerRun}"
           
        }
    
    }   
}