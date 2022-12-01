from django.shortcuts import redirect, render
from .forms import ContatcForm
# Create your views here.


def Home(request):
    if request.method == "POST":
        contactForm = ContatcForm(request.POST)
        if contactForm.is_valid():
            contactForm.save()
            contactForm = ContatcForm()
            Context={"messege":"Thank you for reaching out, We will contact you soon","form":contactForm}
            return render(request,"Home/index.html",context=Context)
        else:
            contactForm = ContatcForm()
            Context={"messege":"Something Went Wrong,Please Fill up All the fields and then submit","form":contactForm}
            return render(request,"Home/index.html",context=Context)
    else:
        contactForm = ContatcForm()
        Context={"form":contactForm}
    return render(request,"Home/index.html",context=Context)