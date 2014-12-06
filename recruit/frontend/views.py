import docker, json
from django.shortcuts import render
from recruit.applications.models import Application

def test(request, image, username, key):
    c = docker.Client(base_url='unix://var/run/docker.sock', version='1.15')
    a = Application.objects.create_application(image, username, key)

    if not a.container:
        env = {'USER': username, 'PASS': a.password}
        cmd = '/user.sh'
        name = image + '-' + key
        image_name = a.test_image.image + ':' + a.test_image.tag

        container = c.create_container(image=image_name, command=cmd, name=name, environment=env)
        a.container = container['Id']
        a.save()

        c.execute(a.container, cmd)

    return render(request, 'frontend/test.html')

def attempt(request, container):
    pass