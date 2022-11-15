from django.shortcuts import render

# Create your views here.
def lobby(request):
    template_name = 'chat/lobby.html'
    return render(request=request, template_name=template_name)