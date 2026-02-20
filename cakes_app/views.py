from django.shortcuts import render, redirect, get_object_or_404

from cakes_app.forms import CakeForm
from cakes_app.models import Cake, Baker


# Create your views here.
def index(request):
    cakes = Cake.objects.all()
    return render(request, template_name="index.html", context={"cakes": cakes})

def add(request):
    print("add===============================================")

    if request.method == "POST":
        print("POST data:", request.POST)
        form = CakeForm(request.POST, request.FILES)
        print("Form valid:", form.is_valid())
        print("Form errors:", form.errors)
        if form.is_valid():
            cake = form.save(commit=False)
            print("Cake before save:", cake.name, cake.baker)
            cake.save()
            print("Saved cake:", cake.name, cake.id)
            return redirect("index")

    elif request.method == "GET":
        form = CakeForm()
        return render(request, template_name="details.html", context={"form": form})
    
    return redirect("index")

def edit(request, cake_id):
    print("edit===============================")
    cake = Cake.objects.filter(id=cake_id).first()
    if request.method == "POST":
        form = CakeForm(request.POST, request.FILES, instance=cake)
        if form.is_valid():
            cake = form.save(commit=False)
            cake.baker = form.cleaned_data['baker']
            cake.save()
            return redirect("index")

    elif request.method == "GET":
        form = CakeForm(instance=cake)
        return render(request, template_name="details.html", context={"cake": cake, "form": form})
    
    return redirect("index")

def delete(request, cake_id):
    cake = get_object_or_404(Cake, id=cake_id)
    cake.delete()
    return redirect("index")