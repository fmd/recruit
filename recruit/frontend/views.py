from django.shortcuts import render

def test(request, image, username, key):
    a = Application.objects.create_application(image, username, key)
    return render(request, 'frontend/test.html')