from django.shortcuts import render


def index(request):
    if request.method =="GET":
        vysledok = 0
    if request.method == "POST":
        a = int(request.POST["a"])
        b = int(request.POST["b"])
        
    

        if a >b :
            vysledok = a 
        elif b >a :
            vysledok = b
        else:
            vysledok = "cisla sa rovnaju "
   




            return render(request, 'cisla/index.html',{"vysledok":vysledok})
