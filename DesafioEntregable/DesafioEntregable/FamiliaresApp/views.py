from django.shortcuts import render



from FamiliaresApp.models import familiar

def Mi_familia (request):
    familia=  familiar.objects.all()
    
    cxt={"familiar":familia}
    return render(request, "index.html", cxt )