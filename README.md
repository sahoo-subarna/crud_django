python3 -m venv e1

source e1/bin/activate

pip3 install django



pip3 freeze

pip3 freeze > requirements.txt



django-admin startproject core

django-admin startapp crud  

python3 manage.py migrate # before creating superuser

python3 manage.py createsuperuser



python3 manage.py makemigrations
python3 manage.py migrate 

# admin.site.register(Task)



# GIT Commands -:

 git clone https://github.com/subarna-sahoo/task_project.git