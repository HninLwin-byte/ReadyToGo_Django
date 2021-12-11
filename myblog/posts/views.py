from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html',{'posts':posts})

def reservation(request):
    
    return render(request,'reservation.html')

def home(request):
    return render(request,'home.html')
'''def reservation(request):
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_number = request.POST['people']

        send_mail(
            message_name,
            message_number,
            message_email,
            ['hninlwin171@gmail.com'])
        return render(request, 'reservation.html', {})
        

    else:
      return render(request, 'reservation.html',{})
    return render(request,'reservation.html' )'''

class TesView(APIView):
    def get(self, request, *args, **kargs):
        data = {
            'username': 'admin' ,
            'num_of_reservation' : 5

        }
        return Response(data)