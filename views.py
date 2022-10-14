from django.shortcuts import render


from .models import directores
def index(request):
  
    directore=directores.objects.all()
    


    return render(
        request,
        'index.html',
           
        context={
            
            'directores':directore
            
        }
            
    )
   