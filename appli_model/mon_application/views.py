from django.shortcuts import render, redirect
from .forms import ExempleModelForm
from .models import ExempleModel
from datetime import datetime  # Assurez-vous que cette ligne est présente

def exemple_model_view(request):
    if request.method == 'POST':
        form = ExempleModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('exemple_model')  # Redirection après soumission
    else:
        form = ExempleModelForm()

    context = {
        'form': form,
        'donnees': ExempleModel.objects.all()  # Récupère tous les objets
    }
    return render(request, 'mon_app/exemple_model.html', context)

def liste_objets(request):
    objets = ExempleModel.objects.all()  # Récupère tous les objets du modèle ExempleModel
    context = {
        'exemples': objets,
        'year': datetime.now().year,
    }
    return render(request, 'mon_application/liste_objets.html', context)