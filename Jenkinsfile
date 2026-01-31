stage('Run all tests') {
    steps {
        sh '''
        #!/bin/bash
        . venv/bin/activate
        export PYTHONPATH=$PYTHONPATH:.

        # Запускаємо тільки твої тести, ігноруючи сторонні бібліотеки
        python3 -m pytest --alluredir=allure-results --ignore=venv
        '''
    }
}