from django.shortcuts import render, HttpResponse

# Create your views here.

#una vez definidas las vistas hay que indicar en el archivo settings
#que esta nueva "app" esta instalada para que las cargue, si no no se
#podran linkear nunca

# settings.py --> installed apps
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

# La vista portfolio estara en su propia App Portfolio porque tiene una 
# logica propipa para mostrar proyectos conforme se añadan a la DB

def contact(request):
    return render(request, "core/contact.html")