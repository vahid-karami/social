from django.shortcuts import render
from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, 'home/index.html')
    
    def post(self, request):
        # Handle POST request logic here
        return render(request, 'home/index.html')
    