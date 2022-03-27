pipeline {
	agent any
	environment {
		VERSION = '1.0.0'
		DOCKERHUB_CREDENTIALS = credentials('docker-baoqiangy-credentials')
	}
	stages {
		stage('Build') {
			parallel {
				stage('Build') {
					steps {
						sh 'echo "building the FlaskDemo v.${VERSION} from Git repo"'
					}
                		}
            		}
        	}

        	stage('Test') {
            		steps {
				sh 'pip install -r requirements.txt'
				sh 'python -m pytest'
				input(id: "Image Build", message: "Deploy ${params.project_name}?", ok: 'Build Docker Image')
            		}
        	}

		stage('Build Docker Image')
                {
                        steps {
                                sh 'docker build -t baoqiangy/flaskdemo:latest .'
                        }
                }

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				sh 'docker push baoqiangy/flaskdemo:latest'
			}
		}

        	stage('Deploy')
        	{
           		steps {
				echo "deploying the application"
            		}
        	}
    	}
    	post {
        	always {
			echo 'The pipeline completed'
        	}
        	success {
			echo "FlaskDemo Application Docker Image Built and Pushed to DockerHub Up!!"
			sh 'docker logout'
        	}
        	failure {
			echo 'Build stage failed'
			error('Stopping early…')
        	}
   	}
}

