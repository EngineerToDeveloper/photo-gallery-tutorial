from django.shortcuts import render

from django.forms import modelformset_factory
from .models import Image, Pet
from .forms import ImageForm, PetForm
from django.http import HttpResponseRedirect

def gallery_view(request, pk):
    pet = Pet.objects.get(id=pk)
    return render(request, 'gallery.html', {"pet":pet})

def add_pet_view(request):
    ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=3)

    if request.method == "GET":
        pet_form = PetForm()
        formset = ImageFormSet(queryset=Image.objects.none())
        return render(request, 'index.html', {"pet_form":pet_form, "formset":formset})
    elif request.method == "POST":
        pet_form = PetForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES)

        if pet_form.is_valid() and formset.is_valid():
            pet_obj = pet_form.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    Image.objects.create(image=image, pet=pet_obj)
            return HttpResponseRedirect('/')
        else:
            print(pet_form.errors, formset.errors)
