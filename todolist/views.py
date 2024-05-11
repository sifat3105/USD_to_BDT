from django.shortcuts import render

# Create your views here.
def dolist_func(request):
    if request.method == 'post':
        
        name = request.POST.get('name')
        age = request.POST.get('age')
        
        if Humans.objects.filter(name=name).exists():
            massage = 'Already Data Exist'
        else:
            human = Humans.objects.create(name=name, age=age,)
            human.save()
    all_data = Humans.objects.all()
    
    return render(request,'dolist.html',locals())
