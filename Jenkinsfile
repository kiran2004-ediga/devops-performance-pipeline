pipeline {
    agent any

    environment {
        JMETER_PATH = "D:\\apache-jmeter-5.6.3\\apache-jmeter-5.6.3\\bin\\jmeter.bat"
        DOCKER_IMAGE = "devops-app"
    }

    stages {

        stage('Clone Code') {
            steps {
                echo "Cloning repository..."
                git 'https://github.com/kiran2004-ediga/devops-performance-pipeline.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                bat 'docker build -t %DOCKER_IMAGE% ./docker'
            }
        }

        stage('Run Application') {
            steps {
                echo "Starting application container..."
                bat 'docker run -d -p 5000:5000 %DOCKER_IMAGE%'
                bat 'timeout /t 10'
            }
        }

        stage('Run Performance Test (JMeter)') {
            steps {
                echo "Running JMeter test..."
                bat '"%JMETER_PATH%" -n -t jmeter\\test-plan.jmx -l results.jtl'
            }
        }

        stage('Evaluate Results') {
            steps {
                echo "Evaluating performance results..."
                bat '''
                findstr "false" results.jtl > errors.txt
                if %ERRORLEVEL%==0 (
                    echo "Performance Test FAILED"
                    exit /b 1
                ) else (
                    echo "Performance Test PASSED"
                )
                '''
            }
        }

        stage('Deploy (Only if Passed)') {
            when {
                expression { currentBuild.currentResult == 'SUCCESS' }
            }
            steps {
                echo "Deploying application..."
                bat 'echo Deployment Successful!'
            }
        }
    }

    post {
        always {
            echo "Cleaning up containers..."
            bat 'docker stop $(docker ps -q)'
            bat 'docker rm $(docker ps -aq)'
        }

        success {
            echo "Pipeline completed successfully 🎉"
        }

        failure {
            echo "Pipeline failed ❌"
        }
    }
}