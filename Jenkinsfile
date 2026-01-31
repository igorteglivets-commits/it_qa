stage('Run all tests') {
    steps {
        sh '''
        #!/bin/bash
        . venv/bin/activate
        
        # Додаємо поточну папку в шлях пошуку модулів
        export PYTHONPATH=$PYTHONPATH:. 
        
        # Запускаємо pytest. Флаг -v покаже, які саме тести знайдені
        # Якщо тестів немає в якійсь папці, pytest просто їх пропустить
        python -m pytest --alluredir=allure-results -v
        '''
    }
}