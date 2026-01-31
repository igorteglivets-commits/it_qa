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
                # Встановлюємо залежності + Playwright
                pip install -r requirements.txt pytest allure-pytest playwright
                # Встановлюємо браузери (без цього Playwright не запрацює в Jenkins)
                python -m playwright install chromium --with-deps
                '''
            }
        }

        stage('Run all tests') {
            steps {
                sh '''
                #!/bin/bash
                . venv/bin/activate
                export PYTHONPATH=$PYTHONPATH:$PWD

                # ГОЛОВНА ЗМІНА: прибрали $(find ...), додали --ignore=venv
                # --continue-on-collection-errors дозволить зібрати звіт, навіть якщо hw_14 не валідний
                python3 -m pytest --alluredir=allure-results --ignore=venv --continue-on-collection-errors
                '''
            }
        }
    }

    post {
        always {
            // Це змусить Jenkins робити звіт незалежно від результату тестів
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}