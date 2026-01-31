stage('Run all tests') {
    steps {
        sh '''
        #!/bin/bash
        . venv/bin/activate
        export PYTHONPATH=$PYTHONPATH:.


        python3 -m pytest --alluredir=allure-results --continue-on-collection-errors
        '''
    }
}