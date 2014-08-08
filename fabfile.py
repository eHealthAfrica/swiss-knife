import os

from fabric.api import *

#env.hosts = ['ubuntu@10.211.55.6']

path, project_name = os.path.split(os.getcwd())
git_repo_remote = 'https://github.com/eHealthAfrica/swiss-knife.git'

@task
def install_dependancies():
    # To avoid password prompt manually add the following to the
    # /etc/sudoers. Use sudo visudo to edit it
    # ubuntu ALL=(ALL) NOPASSWD: ALL
    sudo("apt-get update")
    sudo("apt-get -y install build-essential")
    sudo("apt-get -y install python-dev")

    sudo("apt-get -y install nginx")
    sudo("apt-get -y install rabbitmq-server")

    # PostgreSQL
    # To configure follow instructions here: https://help.ubuntu.com/community/PostgreSQL
    sudo("apt-get -y install libpq-dev libxml2 libxml2-dev")
    #sudo("apt-get -y install binutils libproj-dev gdal-bin")
    sudo("apt-get -y install postgresql postgresql-contrib postgresql-server-dev-9.3 postgresql-9.3-postgis-2.1")
    #sudo("apt-get -y install pgadmin3")

    sudo("apt-get -y install git-core")
    sudo("apt-get -y install python-setuptools")
    sudo("easy_install pip")
    sudo("pip install virtualenv")

@task
def create_env():
    with cd(project_name):
        run("virtualenv env")

@task
def install_requirements():
    with cd(project_name):
        run("env/bin/pip install -r requirements.txt")

@task
def configure_server():
    with cd(project_name):
        sudo("cp production_files/uwsgi.conf /etc/init/uwsgi.conf")
        sudo("cp production_files/nginx_example /etc/nginx/sites-available")
        with settings(warn_only=True):
            sudo("rm /etc/nginx/sites-enabled/default")
            sudo("ln -s /etc/nginx/sites-available/nginx_example /etc/nginx/sites-enabled/nginx_example")
        sudo("cp production_files/celery.conf /etc/init/celery.conf")

@task
def reload_services():
    sudo("service nginx reload")
    sudo("service uwsgi reload")
    sudo("service celery restart")

@task
def restart_services():
    sudo("service nginx restart")
    sudo("service uwsgi restart")
    sudo("service celery restart")

@task
def first_deploy():
    install_dependancies()
    # Avoid rsa prompt
    run('echo -e "Host github.com\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config')
    run("git clone %s" %git_repo_remote)
    create_env()
    install_requirements()
    # Install DB by hand and then syncdb and migrate
    # with cd(project_name):
    #     run("python manage.py syncdb")
    #     run("python manage.py migrate")
    configure_server()
    restart_services()

@task
def pull():
    with cd(project_name):
        run("git pull origin master")

@task
def deploy():
    pull()
    with cd(project_name):
        run("python manage.py syncdb")
        run("python manage.py migrate")
    install_requirements()
    reload_services()

@task
def auto_deploy():
    local_dir_name = os.path.dirname(os.path.realpath(__file__))
    local("cd %s; git pull origin master" %local_dir_name)
    local("cd %s; env/bin/pip install -r requirements.txt" %local_dir_name)
    local("sudo service nginx reload")
    local("sudo service uwsgi reload")
    local("sudo service celery restart")
