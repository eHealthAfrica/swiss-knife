import os

from fabric.api import *

#env.hosts = ['ubuntu@10.211.55.6']

path, project_name = os.path.split(os.getcwd())
git_repo_remote = 'https://github.com/samufuentes/swiss_knife.git'

@task
def install_dependancies():
    # To avoid password prompt manually add the following to the
    # /etc/sudoers. Use sudo visudo to edit it
    # ubuntu ALL=(ALL) NOPASSWD: ALL

    sudo("apt-get -y install build-essential")
    sudo("apt-get -y install python-dev")

    sudo("apt-get -y install nginx")
    sudo("apt-get -y install rabbitmq-server")

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
    configure_server()
    restart_services()

@task
def pull():
    with cd(project_name):
        run("git pull origin master")

@task
def deploy():
    pull()
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
