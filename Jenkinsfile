pipeline {
    agent any 
    stages {
        stage('Stage 1') {
            steps {
                dir

               

                curl https://www.python.org/ftp/python/3.14.0/python-3.14.0a1-amd64.exe --output python.exe

                dir

                python.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

                timeout 60

                py -m pip install Django==5.2.1


                timeout 60

                python manage.py runserver
            }
        }
    }
}