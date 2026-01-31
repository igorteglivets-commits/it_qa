pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/igorteglivets-commits/it_qa.git'
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                #!/bin/bash
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt pytest allure-pytest playwright
                python3 -m playwright install chromium --with-deps
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                #!/bin/bash
                . venv/bin/activate
                export PYTHONPATH=$PYTHONPATH:.


                python3 -m pytest --alluredir=allure-results --ignore=venv
                '''
            }
        }
    }

    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}