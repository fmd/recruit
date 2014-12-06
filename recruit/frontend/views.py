import docker
from django.shortcuts import render
from recruit.applications.models import Application

def test(request, image, username, key):
    c = docker.Client(base_url='unix://var/run/docker.sock')
    a = Application.objects.create_application(image, username, key)

    env = {'USER': username, 'PASS': a.password}
    cmd = '/user.sh'
    name = image + '-' + key

    container = c.create_container(image=a.image.label + ':' + a.image.tag, command=cmd, name=name, environment=env)
    c.execute(container)

    return render(request, 'frontend/test.html')

def attempt(request, container):
    pass