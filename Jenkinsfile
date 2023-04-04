pipeline{
	agent any
	
	triggers{
		githubPush()
	}
	
	stages {
		stage('Checkout'){
			steps{
				checkout([$class: 'GitSCM', branches: [[name: 'main']], userRemoteConfigs: [[url: 'https://github.com/amajps/calcu-api-python']]]) 
			}
		}
	
		stage ('build'){
			steps{
				sh 'docker build -t calc:latest .'
			}
		}
	
		stage('test'){
			steps{
				sh 'docker run -d -p 8000:8000 calc:latest'
				sh 'sleep 60'
				sh 'curl -d "num1=10&num2=13" -X POST http://localhost:8000/mult'
				sh 'docker stop $(docker ps -q --filter ancestor=calc)'
			}	
		}	
	}
}


